from __future__ import annotations

import re
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source_material" / "radar"
DOCS_DIR = ROOT / "docs"
SCHEMA_PATH = ROOT / "schemas" / "src-radar.schema.yaml"


RANGE_CODE_TO_KM = {
    "01": 1.5,
    "02": 2,
    "03": 3,
    "04": 4,
    "05": 5,
    "08": 8,
    "10": 10,
    "12": 12,
    "16": 16,
    "25": 25,
    "50": 50,
}

BAND_NAMES = {"C": "C band", "X": "X band", "K": "Ku band"}
ARCH_NAMES = {
    "A": "Electronic Azimuth Scanning",
    "B": "Mechanical Azimuth Scanning + Electronic Elevation Steering",
    "C": "2D Electronic Scanning (Single-Face AESA)",
    "D": "Electronic Scanning with Mechanical Rotation",
    "E": "Four-Face AESA Array",
}
WAVEFORM_BY_GENERATION = {
    "1": ("P", "Pulse Doppler"),
    "2": ("F", "FMCW"),
    "3": ("P", "Pulse Doppler"),
}
PURPOSE_LABELS = {
    "D": "drone detection",
    "G": "ground surveillance",
    "M": "multi-purpose surveillance",
}

TEXT_REPLACEMENTS = {
    "：": ":",
    "（": "(",
    "）": ")",
    "，": ",",
    "≥": ">=",
    "≤": "<=",
    "â‰¥": ">=",
    "â‰¤": "<=",
    "ï¼œ": "<",
    "ï¼ž": ">",
    "ï¼š": ":",
    "ï¼ˆ": "(",
    "ï¼‰": ")",
    "～": "~",
    "℃": "°C",
    "Â°": "°",
    "â‰¥": ">=",
    "â‰¤": "<=",
    "â„ƒ": "°C",
    "ï½ž": "~",
    "ï¼š": ":",
    "ï¼ˆ": "(",
    "ï¼‰": ")",
    "ã€€": " ",
    "ãŽ¡": "m2",
    "mÂ²": "m²",
    "ï¼Œ": ",",
    "â€”": "-",
    "â€“": "-",
    "Â±": "±",
    "Ituses": "It uses",
}


def fix_text(value: str) -> str:
    text = value
    for bad, good in TEXT_REPLACEMENTS.items():
        text = text.replace(bad, good)
    return text.strip()


def parse_front_matter(lines: list[str]) -> tuple[dict, str]:
    meta: dict[str, object] = {"targets": {}}
    allowed = {"model", "highlight", "range_km", "image", "factory_location"}
    i = 0

    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        if not line:
            i += 1
            continue
        if line == "targets:":
            i += 1
            targets: dict[str, float] = {}
            while i < len(lines):
                match = re.match(r"^\s+([A-Za-z_]+):\s*([0-9.]+)\s*$", lines[i])
                if not match:
                    break
                targets[match.group(1)] = float(match.group(2))
                i += 1
            meta["targets"] = targets
            continue
        match = re.match(r"^([a-z_]+):\s*(.+)$", line)
        if not match or match.group(1) not in allowed:
            break
        key = match.group(1)
        value = match.group(2).strip()
        if key == "range_km":
            meta[key] = float(value)
        else:
            meta[key] = value
        i += 1

    body = "\n".join(lines[i:]).strip()
    return meta, body


def extract_model_parts(model: str) -> dict[str, object]:
    match = re.match(r"^SRC-([CXK])([0-9]{2})([A-E])-([123])([DGM])$", model)
    if not match:
        raise ValueError(f"Unexpected model format: {model}")
    band_code, range_code, arch_code, gen_code, purpose_code = match.groups()
    nominal_class = RANGE_CODE_TO_KM[range_code]
    waveform_code, waveform_name = WAVEFORM_BY_GENERATION[gen_code]
    return {
        "band_code": band_code,
        "range_code": range_code,
        "arch_code": arch_code,
        "gen_code": gen_code,
        "purpose_code": purpose_code,
        "nominal_class_km": nominal_class,
        "waveform_code": waveform_code,
        "waveform_name": waveform_name,
    }


def find_between(text: str, start_patterns: list[str], end_patterns: list[str]) -> str:
    start = None
    for pattern in start_patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            start = match.end()
            break
    if start is None:
        return ""

    end = len(text)
    for pattern in end_patterns:
        match = re.search(pattern, text[start:], flags=re.IGNORECASE)
        if match:
            end = min(end, start + match.start())
    return text[start:end].strip()


def extract_title_phrase(text: str, model: str) -> str:
    pattern = rf"\b(The\s+)?({re.escape(model)}[^.\n]+?)\s+is\b"
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if match:
        phrase = match.group(2).strip()
        return phrase[0].upper() + phrase[1:]
    return f"{model} Surveillance Radar"


def extract_intro(text: str) -> str:
    section = find_between(
        text,
        [r"Product overview:\s*", r"Product Introduction:\s*", r"Product Introduction：\s*"],
        [r"I\.\s*Product Features", r"Product features:\s*", r"Product Advantages:\s*", r"Products parameter", r"Key Specifications:\s*"],
    )
    if section:
        normalized = " ".join(section.split())
        if normalized.count(":") >= 6 or "\t" in normalized:
            return ""
        return normalized

    snippet = text.split("I. Product Features")[0].split("Products parameter")[0].strip()
    normalized = " ".join(snippet.split())
    table_hints = (
        "Type ",
        "Frequency band",
        "Detection range",
        "Blind zone",
        "View range",
        "Track Accuracy",
        "Power Consumption",
    )
    if "\t" in snippet or sum(hint.lower() in normalized.lower() for hint in table_hints) >= 3:
        return ""
    return normalized


def split_sentences(block: str) -> list[str]:
    if not block:
        return []
    parts = re.split(r"(?:\n+|(?<=[.;])\s+)", block)
    cleaned = []
    for part in parts:
        text = " ".join(part.split()).strip(" -:\t")
        if len(text) >= 18:
            cleaned.append(text)
    return cleaned


def extract_feature_sentences(text: str) -> list[str]:
    section = find_between(
        text,
        [r"I\.\s*Product Features\s*", r"Product features:\s*", r"Product Advantages:\s*"],
        [r"II\.\s*Product Specifications", r"Products parameter", r"Key Specifications:\s*", r"Application Scenarios:\s*"],
    )
    return split_sentences(section)


def extract_application_scenarios(text: str) -> list[str]:
    match = re.search(r"Application Scenarios:\s*(.+)", text, flags=re.IGNORECASE)
    if not match:
        return []
    raw = match.group(1)
    items = [item.strip(" .") for item in raw.split(",")]
    return [item for item in items if item]


def parse_number(patterns: list[str], text: str) -> float | None:
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None


def parse_range(patterns: list[str], text: str) -> tuple[float | None, float | None]:
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return float(match.group(1)), float(match.group(2))
    return None, None


def parse_dimensions(text: str) -> dict[str, float] | None:
    match = re.search(r"([0-9.]+)\s*[xX\*]\s*([0-9.]+)\s*[xX\*]\s*([0-9.]+)\s*mm", text, flags=re.IGNORECASE)
    if not match:
        return None
    return {
        "length": float(match.group(1)),
        "width": float(match.group(2)),
        "height": float(match.group(3)),
    }


def estimate_rotation_rpm(interval_s: float | None) -> float | int | None:
    if interval_s is None or interval_s <= 0:
        return None
    estimated = round(60 / interval_s, 1)
    if abs(estimated - round(estimated)) < 0.05:
        return int(round(estimated))
    return estimated


def span_to_coverage(low: float, high: float) -> float:
    if low < 0 <= high:
        return abs(low) + abs(high)
    return abs(high - low)


def parse_azimuth_coverage(text: str) -> float | None:
    half_span = parse_number([r"Azimuth\s*:\s*[±\+/-]?\s*([0-9.]+)\s*°"], text)
    if "±" in text and half_span is not None:
        return half_span * 2

    for pattern in [
        r"Azimuth Coverage\s*[:\t]\s*(?:>=)?\s*([0-9.]+)\s*°",
        r"Scanning Range\s*([0-9.]+)\s*°\s*Azimuth",
        r"Azimuth\s*:\s*(-?[0-9.]+)\s*°\s*~\s*(-?[0-9.]+)\s*°",
        r"([0-9.]+)\s*°\s*azimuth",
    ]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if not match:
            continue
        if len(match.groups()) == 1:
            return float(match.group(1))
        return span_to_coverage(float(match.group(1)), float(match.group(2)))
    return None


def parse_elevation_coverage(text: str) -> float | None:
    for pattern in [
        r"Elevation Coverage\s*[:\t]\s*(-?[0-9.]+)\s*°\s*~\s*(-?[0-9.]+)\s*°",
        r"Elevation\s*:\s*(-?[0-9.]+)\s*°\s*~\s*(-?[0-9.]+)\s*°",
    ]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return span_to_coverage(float(match.group(1)), float(match.group(2)))

    return parse_number(
        [
            r"Elevation Coverage\s*[:\t]\s*(?:>=)?\s*([0-9.]+)\s*°",
            r"([0-9.]+)\s*°\s*elevation range",
        ],
        text,
    )


def parse_accuracy_metric(text: str, label: str) -> float | None:
    return parse_number(
        [
            rf"{label}\s*:\s*(?:<=|<|=)?\s*([0-9.]+)\s*(?:m|°)?",
            rf"{label}\s+accuracy\s*(?:<=|<|=)?\s*([0-9.]+)\s*(?:m|°)?",
        ],
        text,
    )


def parse_refresh_and_rotation(text: str, arch_code: str) -> tuple[float | None, object, object]:
    refresh_matches = re.findall(r"([0-9.]+)\s*s\s*\((\d+)\s*rpm", text, flags=re.IGNORECASE)
    if refresh_matches:
        intervals = [float(item[0]) for item in refresh_matches]
        rpms = [int(item[1]) for item in refresh_matches]
        default_rpm = rpms[0]
        return intervals[0], default_rpm, sorted(set(rpms))

    rpm_values = re.findall(r"(\d+)\s*RPM", text, flags=re.IGNORECASE)
    if rpm_values:
        rpms = [int(item) for item in rpm_values]
        return None, rpms[0], sorted(set(rpms))

    interval = parse_number([r"Data Interval\s*[:\t]\s*([0-9.]+)\s*s", r"Refresh Rate\s*[:\t]\s*([0-9.]+)\s*s"], text)
    if interval is not None:
        if arch_code in {"A", "C", "E"}:
            return interval, "N/A", "N/A"
        estimated_rpm = estimate_rotation_rpm(interval)
        return interval, estimated_rpm, [estimated_rpm] if estimated_rpm is not None else None

    target_update_interval = parse_number(
        [
            r"Target update rate\s*[:\t]?\s*Mechanical scanning\s*(?:<=|<|=)?\s*([0-9.]+)\s*s",
            r"Target update rate\s*[:\t]?\s*TWS\s*[:\t]?\s*(?:<=|<|=)?\s*([0-9.]+)\s*s",
            r"Target update rate\s*[:\t]?\s*([0-9.]+)\s*s",
        ],
        text,
    )
    if target_update_interval is not None:
        if arch_code in {"A", "C", "E"}:
            return target_update_interval, "N/A", "N/A"
        estimated_rpm = estimate_rotation_rpm(target_update_interval)
        return target_update_interval, estimated_rpm, [estimated_rpm] if estimated_rpm is not None else None

    rate_hz = parse_number([r"Data rate\s*>=\s*([0-9.]+)\s*Hz"], text)
    if rate_hz:
        interval = round(1 / rate_hz, 4)
        if arch_code in {"A", "C", "E"}:
            return interval, "N/A", "N/A"
        estimated_rpm = estimate_rotation_rpm(interval)
        return interval, estimated_rpm, [estimated_rpm] if estimated_rpm is not None else None

    if arch_code in {"A", "C", "E"}:
        return None, "N/A", "N/A"
    return None, None, None


def infer_target_domains(purpose_code: str, targets: dict[str, float], text: str) -> list[str]:
    domains: list[str] = []
    lowered = text.lower()
    if purpose_code == "D":
        domains.append("air")
    elif purpose_code == "G":
        domains.append("ground")
    else:
        domains.extend(["ground", "air"])

    if any(key in targets for key in ("person", "vehicle")) and "ground" not in domains:
        domains.append("ground")
    if "vessel" in targets or "ship" in lowered or "maritime" in lowered or "coastal" in lowered:
        domains.append("maritime")
    if "drone_small" in targets and "air" not in domains:
        domains.append("air")
    return domains


def infer_primary_target_types(targets: dict[str, float], purpose_code: str, text: str) -> list[str]:
    items: list[str] = []
    lowered = text.lower()
    if "drone_small" in targets or purpose_code in {"D", "M"}:
        items.append("small_uav")
    if "aircraft" in lowered or "uavs" in lowered or "uav" in lowered:
        if "fixed_wing_uav" not in items:
            items.append("fixed_wing_uav")
    if "person" in targets or "personnel" in lowered:
        items.append("human")
    if "vehicle" in targets or "vehicle" in lowered:
        items.append("vehicle")
    if "vessel" in targets or "ship" in lowered or "maritime" in lowered:
        items.append("boat")
    return items or (["human"] if purpose_code == "G" else ["small_uav"])


def map_detection_targets(targets: dict[str, float], purpose_code: str, nominal_class_km: float) -> tuple[dict[str, float | str], str, float]:
    mapped: dict[str, float | str] = {}
    reference_type = "small_uav"
    reference_rcs = 0.01

    if "drone_small" in targets:
        mapped["small_uav_0_01m2"] = targets["drone_small"]
    if "person" in targets:
        mapped["human_0_5m2"] = targets["person"]
    if "vehicle" in targets:
        mapped["vehicle_2m2"] = targets["vehicle"]
    if "vessel" in targets:
        mapped["boat_10m2"] = targets["vessel"]

    if purpose_code == "G":
        reference_type = "human"
        reference_rcs = 0.5
        mapped.setdefault("human_0_5m2", nominal_class_km)
    else:
        mapped.setdefault("small_uav_0_01m2", nominal_class_km)

    return mapped, reference_type, reference_rcs


def infer_deployment_type(text: str, weight_kg: float | None, arch_code: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ("portable", "rapid deployment", "portable operation", "withdrawal", "lightweight")):
        return "portable"
    if arch_code in {"A", "B", "D"} and weight_kg is not None and weight_kg <= 80:
        return "portable"
    return "fixed"


def infer_use_cases(purpose_code: str, application_scenarios: list[str], targets: dict[str, float], text: str) -> tuple[list[str], list[str]]:
    if application_scenarios:
        primary = application_scenarios[:3]
    elif purpose_code == "D":
        primary = ["low-altitude surveillance", "critical site protection", "counter-UAS early warning"]
    else:
        primary = ["land border surveillance", "critical site protection", "maritime surveillance" if "vessel" in targets or "maritime" in text.lower() else "perimeter monitoring"]

    secondary = []
    lowered = text.lower()
    if "electro-optical" in lowered or "electro optical" in lowered:
        secondary.append("electro-optical cueing")
    if "bird" in lowered:
        secondary.append("bird activity monitoring")
    if "multi-target" in lowered or "multi target" in lowered:
        secondary.append("dense target monitoring")
    if not secondary:
        secondary.append("cooperative multi-sensor detection")
    return primary, secondary


def build_key_features(feature_lines: list[str], text: str, waveform_name: str, azimuth_cov: float | None, elevation_cov: float | None, tws: int | None) -> list[str]:
    features: list[str] = []
    for item in feature_lines:
        sentence = item.rstrip(".")
        if sentence and sentence not in features:
            features.append(sentence + ".")
        if len(features) == 4:
            break

    if len(features) < 3:
        if waveform_name == "FMCW":
            features.append("FMCW operation with low transmission power and strong continuity on small-target detection.")
        else:
            features.append("Pulse Doppler architecture for stable target detection and tracking in security surveillance scenarios.")
    if len(features) < 3 and azimuth_cov is not None:
        elev_text = f" and {elevation_cov:g} degree elevation coverage" if elevation_cov is not None else ""
        features.append(f"{azimuth_cov:g} degree azimuth coverage{elev_text} for wide-area surveillance.")
    if len(features) < 3 and tws is not None:
        features.append(f"Supports up to {tws} simultaneous tracked targets.")
    if len(features) < 3:
        features.append("Designed for all-day, all-weather operation in complex environments.")
    if len(features) < 3:
        features.append("Provides stable surveillance performance for security monitoring and target awareness.")
    if len(features) < 3:
        features.append("Built for practical deployment, continuous tracking, and integration with response workflows.")
    return features[:4]


def build_yaml_record(path: Path) -> dict[str, object]:
    raw_lines = [fix_text(line.rstrip("\n")) for line in path.read_text(encoding="utf-8").splitlines()]
    meta, body = parse_front_matter(raw_lines)
    model = str(meta["model"])
    parts = extract_model_parts(model)

    title_phrase = extract_title_phrase(body, model)
    intro = extract_intro(body)
    feature_lines = extract_feature_sentences(body)
    app_scenarios = extract_application_scenarios(body)

    azimuth_cov = parse_number(
        [
            r"Azimuth Coverage\s*[:\t]\s*(?:>=)?\s*([0-9.]+)\s*°",
            r"Scanning Range\s*([0-9.]+)\s*°\s*Azimuth",
            r"View range\s*Azimuth[:：]\s*0°\s*~\s*([0-9.]+)°",
            r"([0-9.]+)\s*°\s*azimuth",
        ],
        body,
    )

    elevation_cov = None
    elev_span = re.search(r"Elevation Coverage\s*[:\t]\s*(-?[0-9.]+)\s*°\s*~\s*(-?[0-9.]+)\s*°", body, flags=re.IGNORECASE)
    if elev_span:
        low = float(elev_span.group(1))
        high = float(elev_span.group(2))
        elevation_cov = abs(low) + abs(high) if low < 0 else high - low
    if elevation_cov is None:
        elevation_cov = parse_number(
            [
                r"Elevation Coverage\s*[:\t]\s*(?:>=)?\s*([0-9.]+)\s*°",
                r"View range\s*Elevation[:：]\s*0°\s*~\s*([0-9.]+)°",
                r"([0-9.]+)\s*°\s*elevation range",
            ],
            body,
        )

    azimuth_cov = parse_azimuth_coverage(body) or azimuth_cov
    elevation_cov = parse_elevation_coverage(body) or elevation_cov

    speed_min, speed_max = parse_range(
        [
            r"Velocity Measurement Range\s*[:\t]\s*([0-9.]+)\s*[-~]\s*([0-9.]+)\s*m/s",
            r"Detection Radial Velocity Range\s*[:\t]\s*([0-9.]+)\s*[-~]\s*([0-9.]+)\s*m/s",
            r"Speed measuring range\s*([0-9.]+)\s*m/s\s*[-~]\s*([0-9.]+)\s*m/s",
        ],
        body,
    )

    blind_zone = parse_number([r"Blind zone\s*[:\t]\s*(?:<=)?\s*([0-9.]+)\s*m"], body)
    range_accuracy = parse_number([r"Range Accuracy\s*[:\t]\s*(?:<=)?\s*([0-9.]+)\s*m", r"Distance accuracy\s*(?:<=)?\s*([0-9.]+)\s*m"], body)
    azimuth_accuracy = parse_number(
        [
            r"Azimuth Accuracy\s*[:\t]\s*(?:<=)?\s*([0-9.]+)\s*°",
            r"Azimuth:\s*(?:<=)?\s*([0-9.]+)\s*°",
            r"Azimuth accuracy\s*(?:<=)?\s*([0-9.]+)\s*°",
        ],
        body,
    )
    elevation_accuracy = parse_number(
        [
            r"Elevation Accuracy\s*[:\t]\s*(?:<=)?\s*([0-9.]+)\s*°",
            r"Elevation:\s*(?:<=)?\s*([0-9.]+)\s*°",
            r"Elevation accuracy\s*(?:<=)?\s*([0-9.]+)\s*°",
        ],
        body,
    )

    search_accuracy_block = find_between(body, [r"Search Accuracy\s*"], [r"Track Accuracy\s*"])
    track_accuracy_block = find_between(
        body,
        [r"Track Accuracy\s*"],
        [r"Weight\s", r"Power Consumption", r"Power Supply", r"Environmental Adaptability", r"Main Unit Dimensions"],
    )
    accuracy_source = track_accuracy_block or search_accuracy_block or ""
    range_accuracy = parse_accuracy_metric(accuracy_source, "Distance") or range_accuracy
    azimuth_accuracy = parse_accuracy_metric(accuracy_source, "Azimuth") or azimuth_accuracy
    elevation_accuracy = parse_accuracy_metric(accuracy_source, "Elevation") or elevation_accuracy

    data_interval, rotation_speed, rotation_options = parse_refresh_and_rotation(body, parts["arch_code"])
    tws_count = parse_number(
        [
            r"Number of Targets Tracked Simultaneously\s*[:\t]\s*>=?\s*([0-9.]+)",
            r"simultaneously detect up to\s*([0-9.]+)\s*targets",
            r"Simultaneous Tracking Capacity\s*[:\t]\s*>=?\s*([0-9.]+)",
        ],
        body,
    )
    tws_count_int = int(tws_count) if tws_count is not None else None
    tas_count = parse_number([r"TAS Tracking Targets Number\s*[:\t]?\s*(?:>=|>|=)?\s*([0-9.]+)"], body)
    tas_count_int = int(tas_count) if tas_count is not None else None

    temperature_min = parse_number([r"Operating temperature\s*[:\t]\s*(-?[0-9.]+)\s*°C", r"Working temperature\s*(-?[0-9.]+)\s*°C"], body)
    temperature_max = parse_number([r"Operating temperature\s*[:\t]\s*-?[0-9.]+\s*°C\s*to\s*\+?([0-9.]+)\s*°C", r"Working temperature\s*-?[0-9.]+\s*°C\s*[~\-]\s*\+?([0-9.]+)\s*°C"], body)
    if temperature_max is None:
        temp_match = re.search(r"-([0-9.]+)\s*°C\s*[~\-]\s*\+?([0-9.]+)\s*°C", body, flags=re.IGNORECASE)
        if temp_match:
            temperature_min = -float(temp_match.group(1))
            temperature_max = float(temp_match.group(2))

    enclosure_match = re.search(r"(IP[0-9]{2}(?:\s*\([^)]*IP[0-9]{2}[^)]*\))?)", body, flags=re.IGNORECASE)
    enclosure_rating = enclosure_match.group(1) if enclosure_match else None

    weight_kg = parse_number([r"Weight\s*(?:<=)?\s*([0-9.]+)\s*Kg", r"Size/Weight:\s*(?:<=)?\s*([0-9.]+)\s*kg"], body)
    power_consumption = parse_number([r"Power Consumption\s*(?:<=)?\s*([0-9.]+)\s*W", r"power\s*(?:<=)?\s*([0-9.]+)\s*W"], body)
    dimensions = parse_dimensions(body)

    power_input_match = re.search(r"(DC\s*[0-9~\-V ]+\([^)]*adapter[^)]*\)|AC[0-9V~\- ]+|DC\s*[0-9~\-V ]+)", body, flags=re.IGNORECASE)
    power_input = power_input_match.group(1).strip() if power_input_match else None

    comm_match = re.search(r"(Gigabit Ethernet aviation connector|Ethernet\s*\([^)]*\)|RJ45[^.\n]+Ethernet port)", body, flags=re.IGNORECASE)
    data_interfaces = ["Ethernet"] if comm_match else ["Ethernet"]

    targets = meta.get("targets", {})
    assert isinstance(targets, dict)
    detection_ranges, reference_type, reference_rcs = map_detection_targets(targets, parts["purpose_code"], parts["nominal_class_km"])

    target_domains = infer_target_domains(parts["purpose_code"], targets, body)
    primary_target_types = infer_primary_target_types(targets, parts["purpose_code"], body)
    use_cases_primary, use_cases_secondary = infer_use_cases(parts["purpose_code"], app_scenarios, targets, body)
    deployment_type = infer_deployment_type(body, weight_kg, parts["arch_code"])

    key_features = build_key_features(feature_lines, body, parts["waveform_name"], azimuth_cov, elevation_cov, tws_count_int)

    generated_summary = (
        f"{title_phrase} is a {BAND_NAMES[parts['band_code']]} {parts['waveform_name']} surveillance radar "
        f"designed for {PURPOSE_LABELS[parts['purpose_code']]}. "
        f"It uses {ARCH_NAMES[parts['arch_code']].lower()} for practical security monitoring and response workflows."
    )
    summary = intro or generated_summary

    supported_modules = ["Horizon Sense", "Horizon Fusion", "Horizon Track", "Horizon Command"]
    lowered = body.lower()
    if "ai" in lowered or "machine learning" in lowered:
        supported_modules.insert(3, "Horizon AI")

    small_uav_distance = detection_ranges.get("small_uav_0_01m2")
    special_permit_required = isinstance(small_uav_distance, (int, float)) and float(small_uav_distance) >= 10

    record: dict[str, object] = {
        "product_family": "SRC",
        "product_line_name": "Surveillance Radar by Cyrentis",
        "model": model,
        "product_name": title_phrase,
        "status": "active",
        "visibility": "public",
        "featured": False,
        "positioning": {
            "short": f"{BAND_NAMES[parts['band_code']]} {parts['waveform_name']} surveillance radar for {PURPOSE_LABELS[parts['purpose_code']]}.",
            "tagline": f"{parts['waveform_name']} radar for stable target detection and tracking.",
            "primary_role": "security surveillance radar",
            "application_focus": use_cases_primary,
        },
        "naming": {
            "format": "SRC-[Band][DetectionLevel][Architecture]-[Generation][Purpose]",
            "band_code": parts["band_code"],
            "detection_level_code": parts["range_code"],
            "architecture_code": parts["arch_code"],
            "generation_code": parts["gen_code"],
            "purpose_code": parts["purpose_code"],
        },
        "technical_classification": {
            "waveform": {
                "code": parts["waveform_code"],
                "name": parts["waveform_name"],
            },
            "band": {
                "code": parts["band_code"],
                "name": BAND_NAMES[parts["band_code"]],
            },
            "scan_architecture": {
                "code": parts["arch_code"],
                "name": ARCH_NAMES[parts["arch_code"]],
            },
            "target_domains": target_domains,
            "primary_target_types": primary_target_types,
        },
        "detection": {
            "nominal_class_km": parts["nominal_class_km"],
            "reference_target": {
                "type": reference_type,
                "rcs_m2": reference_rcs,
            },
            "typical_detection_ranges_km": detection_ranges,
            "notes": [],
        },
        "performance": {
            "blind_zone_m": blind_zone,
            "horizontal_field_of_view_deg": azimuth_cov,
            "vertical_field_of_view_deg": elevation_cov,
            "speed_measurement_range_mps": {
                "min": speed_min,
                "max": speed_max,
            },
            "rotation_speed_rpm": rotation_speed,
            "rotation_speed_options_rpm": rotation_options,
            "data_update_interval_s": data_interval,
            "tracking_capacity": {
                "tws_count": tws_count_int,
                "tas_count": "N/A" if parts["arch_code"] in {"A", "B"} else tas_count_int,
            },
            "accuracy": {
                "range_m": range_accuracy,
                "azimuth_deg": azimuth_accuracy,
                "elevation_deg": elevation_accuracy,
            },
        },
        "coverage": {
            "azimuth": {
                "mode": "electronic" if parts["arch_code"] in {"A", "C", "E"} else "mechanical" if parts["arch_code"] == "B" else "hybrid",
                "coverage_deg": azimuth_cov,
            },
            "elevation": {
                "mode": "electronic" if parts["arch_code"] in {"A", "B", "C", "D", "E"} else "electronic",
                "coverage_deg": elevation_cov,
            },
            "refresh_rate_s": data_interval,
            "instrumented_range_km": meta.get("range_km"),
        },
        "physical": {
            "deployment_type": deployment_type,
            "enclosure_rating": enclosure_rating,
            "operating_temperature_c": {
                "min": temperature_min,
                "max": temperature_max,
            },
            "dimensions_mm": dimensions or {"length": None, "width": None, "height": None},
            "weight_kg": weight_kg,
        },
        "interfaces": {
            "power_input": power_input,
            "data_interfaces": data_interfaces,
            "power_consumption_w": power_consumption,
            "protocol_support": ["Ethernet"],
            "horizon_compatible": True,
            "third_party_integration": True,
        },
        "platform_integration": {
            "compatible_platforms": ["Cyrentis Horizon"],
            "supported_modules": supported_modules,
            "supports_cueing_to_optics": "electro-optical" in lowered or "electro optical" in lowered or parts["purpose_code"] == "D",
            "supports_multi_sensor_fusion": True,
        },
        "use_cases": {
            "primary": use_cases_primary,
            "secondary": use_cases_secondary,
        },
        "media": {
            "hero_image": meta.get("image"),
        },
        "content": {
            "summary": summary,
            "key_features": key_features,
            "application_scenarios": app_scenarios or use_cases_primary,
        },
        "contact": {
            "inquiry_enabled": True,
            "recommended_cta": "Request radar consultation",
        },
    }

    notes = record["detection"]["notes"]
    assert isinstance(notes, list)
    if not targets:
        notes.append("Target-distance fields were inferred from the model naming code because the source file did not include a structured targets block.")
    if parts["purpose_code"] == "G" and "human_0_5m2" not in detection_ranges:
        notes.append("Ground-surveillance nominal class was converted using the naming code as a human 0.5 m2 reference.")
    if parts["purpose_code"] in {"D", "M"} and "small_uav_0_01m2" not in detection_ranges:
        notes.append("Air or multi-purpose nominal class was converted using the naming code as a small UAV 0.01 m2 reference.")
    if meta.get("range_km") and meta.get("range_km") != parts["nominal_class_km"]:
        notes.append(f"Instrumented range uses the source preamble value {meta['range_km']:g} km, while nominal class follows model code {parts['nominal_class_km']:g} km.")
    if "car" in body.lower() and "vehicle_2m2" not in detection_ranges:
        notes.append("Vehicle detection details in the source use a different RCS bucket than the schema's fixed vehicle_2m2 field.")

    # Remove empty optional note arrays.
    if not notes:
        record["detection"].pop("notes")

    if special_permit_required:
        record["export_compliance"] = {
            "china_regime": "PRC dual-use export control",
            "civil_security_only": True,
            "general_notice": "This product is intended for civil security use only. Export from China is subject to PRC dual-use export control and licensing procedures.",
            "official_basis": [
                "PRC Dual-Use Export Control List (effective 2024-12-01)",
                "MOFCOM / GACC / CMC EDD Announcement No. 31 of 2024",
            ],
            "review_rule": {
                "rule_type": "internal_compliance_escalation_rule",
                "measurement_field": "detection.typical_detection_ranges_km.small_uav_0_01m2",
                "small_uav_threshold_km": 10,
                "triggered": True,
                "control_status": "special_permit_required",
                "license_requirement": "special_permit_required",
                "reviewer_note": "Auto-generated from source text and naming-rule mapping.",
            },
        }

    return record


def main() -> None:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    created = 0
    validated = 0

    for txt_path in sorted(SOURCE_DIR.glob("SRC-*.txt")):
        record = build_yaml_record(txt_path)
        out_path = DOCS_DIR / f"{txt_path.stem}.yaml"
        out_path.write_text(
            yaml.safe_dump(record, sort_keys=False, allow_unicode=False),
            encoding="utf-8",
        )
        created += 1
        data = yaml.safe_load(out_path.read_text(encoding="utf-8"))
        try:
            jsonschema.validate(data, schema)
        except Exception as exc:
            raise RuntimeError(f"Validation failed for {txt_path.name}: {exc}") from exc
        validated += 1

    print(f"created={created}")
    print(f"validated={validated}")


if __name__ == "__main__":
    main()
