from __future__ import annotations

import argparse
import math
import re
import shutil
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[4]
DOCS_DIR = ROOT / "docs"
OUTPUT_DIR = ROOT / "content" / "en" / "sensors" / "src"
LEGACY_DIR = ROOT / "content" / "en" / "complete-products" / "radar"
REF_IMAGE_DIR = ROOT / "static" / "ref-image"

DEFAULT_HERO_IMAGE = "/images/sensors/sample-radar.png"
MOFCOM_LINK = "https://www.mofcom.gov.cn/zfxxgk/fdzdgknr/ztfl/dwmygl/art/2024/art_8300c93ceef047debcf4da0ced080629.html"

TARGET_RANGE_META = [
    ("small_uav_0_01m2", "Small UAV", "/images/icons/radar-target-drone.svg", "0.01 mÂ² reference target"),
    ("fixed_wing_uav_1m2", "Large UAV", "/images/icons/radar-target-vtol.svg", "1 mÂ² fixed-wing reference target"),
    ("human_0_5m2", "Human", "/images/icons/radar-target-person.svg", "0.5 mÂ² reference target"),
    ("vehicle_2m2", "Vehicle", "/images/icons/radar-target-vehicle.svg", "2 mÂ² reference target"),
    ("boat_10m2", "Vessel", "/images/icons/radar-target-vessel.svg", "10 mÂ² reference target"),
]

TARGET_RANGE_LOOKUP = {field: (label, icon, note) for field, label, icon, note in TARGET_RANGE_META}

HERO_TARGET_FIELDS = {
    "G": ["human_0_5m2", "vehicle_2m2", "boat_10m2"],
    "D": ["small_uav_0_01m2", "fixed_wing_uav_1m2"],
}

AZIMUTH_DEFAULTS_BY_ARCHITECTURE = {
    "A": 90.0,
    "B": 360.0,
    "D": 360.0,
    "E": 360.0,
}

ELEVATION_DEFAULTS_BY_ARCHITECTURE = {
    "B": 65.0,
}

MODULE_META = {
    "Horizon Sense": {
        "icon": "/images/horizon/module-sense.svg",
        "text": "Registers the radar as a managed sensing asset with shared device, health, and status context.",
    },
    "Horizon Fusion": {
        "icon": "/images/horizon/module-fusion.svg",
        "text": "Correlates radar detections with adjacent sensing layers so alarms do not remain isolated inside one subsystem.",
    },
    "Horizon Track": {
        "icon": "/images/horizon/module-track.svg",
        "text": "Maintains trajectory continuity and target history as detections move through the monitored scene.",
    },
    "Horizon AI": {
        "icon": "/images/horizon/module-ai.svg",
        "text": "Supports downstream recognition and prioritization when operators need faster interpretation of ambiguous tracks.",
    },
    "Horizon Command": {
        "icon": "/images/horizon/module-command.svg",
        "text": "Pushes alarms, live track state, and operator actions into one command workflow instead of disconnected device screens.",
    },
    "Horizon Notify": {
        "icon": "/images/horizon/module-notify.svg",
        "text": "Routes important events into notification and escalation workflows beyond the main operator console.",
    },
    "Horizon Archive": {
        "icon": "/images/horizon/module-archive.svg",
        "text": "Retains event history, evidence continuity, and replay material for review and after-action analysis.",
    },
    "Horizon Link": {
        "icon": "/images/horizon/module-link.svg",
        "text": "Connects the radar workflow to third-party software, site systems, and broader operational environments.",
    },
}

SCENARIO_IMAGE_META = {
    "industrial": {
        "image": "/images/sensors/deployment-industrial.svg",
        "title": "Industrial campuses",
        "alt": "Line concept illustration of an industrial monitoring site",
    },
    "port": {
        "image": "/images/sensors/deployment-port.svg",
        "title": "Port and waterside assets",
        "alt": "Line concept illustration of a port monitoring site",
    },
    "airport": {
        "image": "/images/sensors/deployment-airport.svg",
        "title": "Airport perimeters",
        "alt": "Line concept illustration of an airport perimeter monitoring site",
    },
}

SPECIAL_COVERAGE_NOTES = {
    "SRC-X10B-2D": {"Vertical Coverage": "-5 to 60 degrees"},
}


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any) -> bool:
        return True


def clean_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = (
        text.replace("mÃ‚Â²", "m²")
        .replace("mÂ²", "m²")
        .replace("Ã‚", "")
        .replace("Â", "")
        .replace("° C", "°C")
    )
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r";\.$", ".", text)
    text = re.sub(r";$", ".", text)
    return text


def meaningful(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return clean_text(value).lower() not in {"", "n/a", "na", "null", "none"}
    return True


def parse_number(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if not meaningful(value):
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", clean_text(value))
    if not match:
        return None
    return float(match.group(0))


def format_number(value: Any) -> str:
    number = parse_number(value)
    if number is None:
        return clean_text(value)
    if float(number).is_integer():
        return str(int(number))
    return f"{number:g}"


def format_distance_km(value: Any) -> str:
    return f"{format_number(value)} km"


def format_angle_deg(value: Any) -> str:
    return f"{format_number(value)}°"


def format_distance_m(value: Any) -> str:
    return f"{format_number(value)} m"


def format_area_km2(value: Any) -> str:
    number = parse_number(value)
    if number is None:
        return clean_text(value)
    if abs(number - round(number)) < 0.05:
        return f"{int(round(number)):,} km²"
    return f"{number:,.1f} km²"


def format_temperature_range(temp_block: dict[str, Any] | None) -> str | None:
    if not temp_block:
        return None
    low = temp_block.get("min")
    high = temp_block.get("max")
    if meaningful(low) and meaningful(high):
        return f"{format_number(low)} to {format_number(high)} °C"
    return None


def format_speed_range(speed_block: dict[str, Any] | None) -> str | None:
    if not speed_block:
        return None
    low = speed_block.get("min")
    high = speed_block.get("max")
    if meaningful(low) and meaningful(high):
        return f"{format_number(low)} to {format_number(high)} m/s"
    return None


def sentence_case(text: str) -> str:
    text = clean_text(text)
    if not text:
        return text
    return text[0].upper() + text[1:]


def title_case_phrase(text: str) -> str:
    words = re.split(r"[\s/-]+", clean_text(text))
    out: list[str] = []
    for word in words:
        if not word:
            continue
        if word.upper() in {"UAS", "UAV", "EO", "RF", "SRC"}:
            out.append(word.upper())
        elif word.isupper() and len(word) <= 5:
            out.append(word)
        else:
            out.append(word.capitalize())
    return " ".join(out)


def list_join(items: list[str]) -> str:
    items = [clean_text(item) for item in items if clean_text(item)]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def format_list_value(items: list[Any] | None) -> str | None:
    if not isinstance(items, list):
        return None
    cleaned = unique_keep_order([title_case_phrase(clean_text(item)) for item in items if clean_text(item)])
    return ", ".join(cleaned) if cleaned else None


def format_bool(value: Any) -> str | None:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return None


def format_dimensions_mm(dimensions: dict[str, Any] | None) -> str | None:
    if not dimensions:
        return None
    length = dimensions.get("length")
    width = dimensions.get("width")
    height = dimensions.get("height")
    if meaningful(length) and meaningful(width) and meaningful(height):
        return f"{format_number(length)} × {format_number(width)} × {format_number(height)} mm"
    return None


def readable_target_type(value: Any) -> str | None:
    text = clean_text(value).lower()
    if not text:
        return None
    mapping = {
        "small_uav": "Small UAV",
        "fixed_wing_uav": "Large UAV",
        "human": "Human",
        "vehicle": "Vehicle",
        "boat": "Vessel",
    }
    return mapping.get(text, title_case_phrase(text.replace("_", " ")))


def get_purpose_code(data: dict[str, Any]) -> str:
    return clean_text(data.get("naming", {}).get("purpose_code")).upper()


def get_architecture_code(data: dict[str, Any]) -> str:
    return clean_text(data.get("naming", {}).get("architecture_code")).upper()


def get_max_range_number(data: dict[str, Any]) -> float | None:
    instrumented = data.get("coverage", {}).get("instrumented_range_km")
    nominal = data.get("detection", {}).get("nominal_class_km")
    return parse_number(instrumented if meaningful(instrumented) else nominal)


def get_azimuth_coverage_number(data: dict[str, Any]) -> float | None:
    coverage = data.get("coverage", {}) or {}
    performance = data.get("performance", {}) or {}
    architecture_code = get_architecture_code(data)
    return (
        parse_number(coverage.get("azimuth", {}).get("coverage_deg"))
        or parse_number(performance.get("horizontal_field_of_view_deg"))
        or AZIMUTH_DEFAULTS_BY_ARCHITECTURE.get(architecture_code)
    )


def get_elevation_coverage_number(data: dict[str, Any]) -> float | None:
    coverage = data.get("coverage", {}) or {}
    performance = data.get("performance", {}) or {}
    architecture_code = get_architecture_code(data)
    return (
        parse_number(coverage.get("elevation", {}).get("coverage_deg"))
        or parse_number(performance.get("vertical_field_of_view_deg"))
        or ELEVATION_DEFAULTS_BY_ARCHITECTURE.get(architecture_code)
    )


def get_coverage_area_km2(data: dict[str, Any]) -> float | None:
    max_range = get_max_range_number(data)
    azimuth = get_azimuth_coverage_number(data)
    if max_range is None or azimuth is None:
        return None
    return math.pi * (max_range**2) * (azimuth / 360.0)


def infer_range_from_rcs(base_range: Any, base_rcs: float, target_rcs: float, max_range: float | None) -> float | None:
    distance = parse_number(base_range)
    if distance is None:
        return None
    scaled = distance * ((target_rcs / base_rcs) ** 0.25)
    if max_range is not None:
        scaled = min(scaled, max_range)
    return round(scaled, 1)


def get_target_range_value(data: dict[str, Any], field: str) -> float | None:
    ranges = data.get("detection", {}).get("typical_detection_ranges_km") or {}
    direct = ranges.get(field)
    if meaningful(direct):
        return parse_number(direct)

    max_range = get_max_range_number(data)
    if field == "fixed_wing_uav_1m2":
        return infer_range_from_rcs(ranges.get("small_uav_0_01m2"), 0.01, 1.0, max_range)
    if field == "vehicle_2m2":
        return infer_range_from_rcs(ranges.get("human_0_5m2"), 0.5, 2.0, max_range)
    if field == "boat_10m2":
        return infer_range_from_rcs(ranges.get("human_0_5m2"), 0.5, 10.0, max_range)
    return None


def unique_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        cleaned = clean_text(item)
        if cleaned and cleaned.lower() not in seen:
            seen.add(cleaned.lower())
            result.append(cleaned)
    return result


def resolve_ref_image(model: str) -> str:
    candidates = [
        REF_IMAGE_DIR / f"{model}.png",
        REF_IMAGE_DIR / f"{model}-.png",
    ]
    for path in candidates:
        if path.exists():
            return f"/ref-image/{path.name}"
    return DEFAULT_HERO_IMAGE


def feature_title_for_text(text: str, index: int) -> str:
    lower = text.lower()
    if ":" in text:
        head = clean_text(text.split(":", 1)[0])
        if head:
            return head
    if "tracking" in lower:
        return "Track capacity"
    if "false alarm" in lower:
        return "Low false-alarm behavior"
    if "all-weather" in lower or "continuous" in lower:
        return "Continuous surveillance"
    if "accuracy" in lower:
        return "Detection accuracy"
    if "range" in lower or "distance" in lower:
        return "Range coverage"
    if "cost-effective" in lower or "easy to operate" in lower:
        return "Practical deployment"
    if "small target" in lower or "drone" in lower or "uav" in lower:
        return "Small-target detection"
    return f"Operational advantage {index:02d}"


def feature_text_for_item(text: str) -> str:
    if ":" in text:
        return sentence_case(text.split(":", 1)[1])
    return sentence_case(text)


def build_feature_cards(data: dict[str, Any]) -> list[dict[str, str]]:
    raw_features = data.get("content", {}).get("key_features") or []
    cleaned = [clean_text(item) for item in raw_features if clean_text(item)]
    if not cleaned:
        summary = clean_text(data.get("content", {}).get("summary"))
        cleaned = [segment.strip() for segment in re.split(r"(?<=[.!?])\s+", summary) if segment.strip()][:3]
    cards: list[dict[str, str]] = []
    for idx, feature in enumerate(cleaned[:3], start=1):
        cards.append(
            {
                "title": feature_title_for_text(feature, idx),
                "text": feature_text_for_item(feature),
            }
        )
    return cards


def build_hero_stats(data: dict[str, Any]) -> list[dict[str, str]]:
    stats: list[dict[str, str]] = []
    purpose_code = get_purpose_code(data)

    for field in HERO_TARGET_FIELDS.get(purpose_code, []):
        value = get_target_range_value(data, field)
        if value is None:
            continue
        label, icon, note = TARGET_RANGE_LOOKUP[field]
        stats.append(
            {
                "icon": icon,
                "label": label,
                "value": format_distance_km(value),
                "note": clean_text(note),
            }
        )

    max_range = get_max_range_number(data)
    if max_range is not None:
        stats.append(
            {
                "icon": "/images/icons/radar-stat-range.svg",
                "label": "Maximum Range",
                "value": format_distance_km(max_range),
                "note": (
                    "Instrumented site-planning range"
                    if meaningful(data.get("coverage", {}).get("instrumented_range_km"))
                    else "Nominal detection class"
                ),
            }
        )
    return stats


def build_coverage_table(model: str, data: dict[str, Any]) -> list[dict[str, str]]:
    azimuth = get_azimuth_coverage_number(data)
    elevation = get_elevation_coverage_number(data)
    area = get_coverage_area_km2(data)

    entries: list[dict[str, str]] = [
        {
            "label": "Horizontal Coverage",
            "value": format_angle_deg(azimuth) if azimuth is not None else "Not published",
        },
        {
            "label": "Vertical Coverage",
            "value": format_angle_deg(elevation) if elevation is not None else "Not published",
        },
        {
            "label": "Coverage Area",
            "value": format_area_km2(area) if area is not None else "Not published",
            "note": "Computed at maximum range",
        },
    ]

    note = SPECIAL_COVERAGE_NOTES.get(model, {}).get("Vertical Coverage")
    if note:
        entries[1]["note"] = note

    return entries


def build_technical_snapshot(data: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(name: str, value: str | None) -> None:
        if meaningful(value):
            rows.append({"name": name, "value": clean_text(value)})

    classification = data.get("technical_classification", {}) or {}
    detection = data.get("detection", {}) or {}
    performance = data.get("performance", {}) or {}
    coverage = data.get("coverage", {}) or {}
    physical = data.get("physical", {}) or {}
    interfaces = data.get("interfaces", {}) or {}
    platform = data.get("platform_integration", {}) or {}

    add("Operating Band", classification.get("band", {}).get("name"))
    add("Waveform", classification.get("waveform", {}).get("name"))
    add("Scan Architecture", classification.get("scan_architecture", {}).get("name"))
    add("Target Domains", format_list_value(classification.get("target_domains")))
    add(
        "Primary Target Types",
        format_list_value([readable_target_type(item) for item in (classification.get("primary_target_types") or [])]),
    )

    reference_target = detection.get("reference_target", {}) or {}
    reference_type = readable_target_type(reference_target.get("type"))
    reference_rcs = reference_target.get("rcs_m2")
    if reference_type and meaningful(reference_rcs):
        add("Reference Target", f"{reference_type} ({format_number(reference_rcs)} m²)")

    for field, label, _, note in TARGET_RANGE_META:
        value = get_target_range_value(data, field)
        if value is not None:
            add(f"{label} Detection", f"{format_distance_km(value)} ({clean_text(note)})")

    add("Nominal Class", format_distance_km(detection.get("nominal_class_km")) if meaningful(detection.get("nominal_class_km")) else None)
    add(
        "Instrumented Range",
        format_distance_km(coverage.get("instrumented_range_km")) if meaningful(coverage.get("instrumented_range_km")) else None,
    )
    add("Blind Zone", format_distance_m(performance.get("blind_zone_m")) if meaningful(performance.get("blind_zone_m")) else None)
    add("Horizontal Coverage", format_angle_deg(get_azimuth_coverage_number(data)) if get_azimuth_coverage_number(data) is not None else None)
    add("Vertical Coverage", format_angle_deg(get_elevation_coverage_number(data)) if get_elevation_coverage_number(data) is not None else None)
    add("Coverage Area", format_area_km2(get_coverage_area_km2(data)) if get_coverage_area_km2(data) is not None else None)

    refresh = coverage.get("refresh_rate_s") or performance.get("data_update_interval_s")
    add("Refresh Rate", f"{format_number(refresh)} s" if meaningful(refresh) else None)
    add("Velocity Range", format_speed_range(performance.get("speed_measurement_range_mps")))
    add("Range Accuracy", format_distance_m(performance.get("accuracy", {}).get("range_m")) if meaningful(performance.get("accuracy", {}).get("range_m")) else None)
    add("Azimuth Accuracy", format_angle_deg(performance.get("accuracy", {}).get("azimuth_deg")) if meaningful(performance.get("accuracy", {}).get("azimuth_deg")) else None)
    add("Elevation Accuracy", format_angle_deg(performance.get("accuracy", {}).get("elevation_deg")) if meaningful(performance.get("accuracy", {}).get("elevation_deg")) else None)

    add("Rotation Speed", f"{format_number(performance.get('rotation_speed_rpm'))} rpm" if meaningful(performance.get("rotation_speed_rpm")) else None)
    rotation_options = performance.get("rotation_speed_options_rpm")
    if isinstance(rotation_options, list):
        add("Rotation Options", " / ".join(f"{format_number(item)} rpm" for item in rotation_options if meaningful(item)))

    tracking = performance.get("tracking_capacity", {}) or {}
    add("TWS Capacity", format_number(tracking.get("tws_count")) if meaningful(tracking.get("tws_count")) else None)
    add("TAS Capacity", format_number(tracking.get("tas_count")) if meaningful(tracking.get("tas_count")) else None)

    add("Deployment Type", title_case_phrase(physical.get("deployment_type")))
    add("Mounting Options", format_list_value(physical.get("mounting_options")))
    add("Dimensions", format_dimensions_mm(physical.get("dimensions_mm")))
    add("Weight", f"{format_number(physical.get('weight_kg'))} kg" if meaningful(physical.get("weight_kg")) else None)
    add("Enclosure Rating", physical.get("enclosure_rating"))
    add("Operating Temperature", format_temperature_range(physical.get("operating_temperature_c")))

    add("Power Input", interfaces.get("power_input"))
    add(
        "Power Consumption",
        f"{format_number(interfaces.get('power_consumption_w'))} W" if meaningful(interfaces.get("power_consumption_w")) else None,
    )
    add("Data Interfaces", format_list_value(interfaces.get("data_interfaces")))
    add("Protocol Support", format_list_value(interfaces.get("protocol_support")))
    add("Horizon Compatible", format_bool(interfaces.get("horizon_compatible")))
    add("Third-Party Integration", format_bool(interfaces.get("third_party_integration")))
    add("Cueing To Optics", format_bool(platform.get("supports_cueing_to_optics")))
    add("Multi-Sensor Fusion", format_bool(platform.get("supports_multi_sensor_fusion")))
    add("Compatible Platforms", format_list_value(platform.get("compatible_platforms")))
    add("Supported Horizon Modules", format_list_value(platform.get("supported_modules")))

    return rows


def build_integration_modules(data: dict[str, Any]) -> list[dict[str, str]]:
    modules = data.get("platform_integration", {}).get("supported_modules") or []
    results: list[dict[str, str]] = []
    for module in modules:
        info = MODULE_META.get(module)
        if info:
            results.append({"icon": info["icon"], "title": module, "text": info["text"]})
    return results


def scenario_bucket(text: str) -> str:
    lower = text.lower()
    if any(keyword in lower for keyword in ["port", "maritime", "coastal", "waterside", "vessel", "boat"]):
        return "port"
    if any(keyword in lower for keyword in ["airport", "bird", "airspace", "counter-uas", "counter uas", "drone", "low-altitude", "low altitude"]):
        return "airport"
    return "industrial"


def scenario_title(text: str) -> str:
    lower = text.lower()
    if "border" in lower:
        return "Border and perimeter zones"
    if any(keyword in lower for keyword in ["port", "maritime", "coastal", "waterside"]):
        return "Port and maritime watch"
    if any(keyword in lower for keyword in ["airport", "bird", "airspace", "counter-uas", "counter uas", "drone"]):
        return "Airport and low-altitude security"
    if any(keyword in lower for keyword in ["critical", "key site", "industrial", "energy", "facility"]):
        return "Critical site protection"
    return title_case_phrase(text)


def build_deployment_scenarios(data: dict[str, Any]) -> list[dict[str, str]]:
    scenario_texts = []
    scenario_texts.extend(data.get("content", {}).get("application_scenarios") or [])
    scenario_texts.extend(data.get("use_cases", {}).get("primary") or [])
    scenario_texts.extend(data.get("use_cases", {}).get("secondary") or [])
    scenario_texts.extend(data.get("positioning", {}).get("application_focus") or [])
    unique_scenarios = unique_keep_order([clean_text(item) for item in scenario_texts])
    if not unique_scenarios:
        unique_scenarios = ["critical site protection", "layered perimeter surveillance", "coordinated low-altitude monitoring"]

    cards: list[dict[str, str]] = []
    used_titles: set[str] = set()
    for scenario in unique_scenarios:
        bucket = scenario_bucket(scenario)
        meta = SCENARIO_IMAGE_META[bucket]
        title = scenario_title(scenario)
        if title in used_titles:
            continue
        used_titles.add(title)
        cards.append(
            {
                "image": meta["image"],
                "title": title,
                "alt": meta["alt"],
                "text": f"Suitable for {clean_text(scenario).lower()} projects that need radar warning integrated into a broader security workflow.",
            }
        )
        if len(cards) == 3:
            break
    return cards


def naming_code(data: dict[str, Any], key: str) -> str:
    return clean_text(data.get("naming", {}).get(key)).upper()


def max_range_sort_value(data: dict[str, Any]) -> float:
    value = get_max_range_number(data)
    return value if value is not None else 0.0


def build_related_products(data: dict[str, Any], catalog: list[dict[str, Any]]) -> list[dict[str, str]]:
    model = clean_text(data.get("model"))
    base_band = naming_code(data, "band_code")
    base_level = naming_code(data, "detection_level_code")
    base_arch = naming_code(data, "architecture_code")
    base_generation = naming_code(data, "generation_code")
    base_purpose = naming_code(data, "purpose_code")
    base_waveform = clean_text(data.get("technical_classification", {}).get("waveform", {}).get("name"))
    base_domains = {
        clean_text(item).lower()
        for item in (data.get("technical_classification", {}).get("target_domains") or [])
        if clean_text(item)
    }
    base_range = max_range_sort_value(data)

    ranked: list[dict[str, Any]] = []
    for candidate in catalog:
        candidate_model = clean_text(candidate.get("model"))
        if not candidate_model or candidate_model == model:
            continue

        cand_band = naming_code(candidate, "band_code")
        cand_level = naming_code(candidate, "detection_level_code")
        cand_arch = naming_code(candidate, "architecture_code")
        cand_generation = naming_code(candidate, "generation_code")
        cand_purpose = naming_code(candidate, "purpose_code")
        cand_waveform = clean_text(candidate.get("technical_classification", {}).get("waveform", {}).get("name"))
        cand_domains = {
            clean_text(item).lower()
            for item in (candidate.get("technical_classification", {}).get("target_domains") or [])
            if clean_text(item)
        }
        cand_range = max_range_sort_value(candidate)

        same_band = bool(base_band) and cand_band == base_band
        same_level = bool(base_level) and cand_level == base_level
        same_generation = bool(base_generation) and cand_generation == base_generation
        same_purpose = bool(base_purpose) and cand_purpose == base_purpose
        same_waveform = bool(base_waveform) and cand_waveform == base_waveform
        alt_architecture = same_band and same_level and same_generation and same_purpose and bool(cand_arch) and cand_arch != base_arch
        shared_domains = len(base_domains.intersection(cand_domains))

        score = 0
        score += 110 if same_level else 0
        score += 85 if same_band else 0
        score += 70 if same_generation else 0
        score += 70 if same_purpose else 0
        score += 45 if same_waveform else 0
        score += 45 if alt_architecture else 0
        score += min(shared_domains, 2) * 15
        if base_range > 0 and cand_range > 0:
            score += max(0, 18 - int(abs(base_range - cand_range) * 3))

        if score <= 0:
            continue

        if alt_architecture:
            relation = "Same band and range class with an alternate scan architecture."
        elif same_band and same_level:
            relation = "Comparable model in the same band and range class."
        elif same_purpose and same_waveform:
            relation = "Comparable mission-focused model with a similar waveform approach."
        else:
            relation = "Adjacent SRC model for similar deployment planning."

        ranked.append(
            {
                "score": score,
                "model": candidate_model,
                "url": f"/sensors/src/{candidate_model.lower()}/",
                "band": clean_text(candidate.get("technical_classification", {}).get("band", {}).get("name")),
                "system_type": cand_waveform,
                "architecture_name": clean_text(candidate.get("technical_classification", {}).get("scan_architecture", {}).get("name")),
                "max_range": format_distance_km(get_max_range_number(candidate) or 0),
                "description": build_description(candidate),
                "relation": relation,
            }
        )

    ranked.sort(key=lambda item: (-item["score"], item["model"]))
    return [
        {
            "model": item["model"],
            "url": item["url"],
            "band": item["band"],
            "system_type": item["system_type"],
            "architecture_name": item["architecture_name"],
            "max_range": item["max_range"],
            "description": item["description"],
            "relation": item["relation"],
        }
        for item in ranked[:5]
    ]


def build_compliance_notice(data: dict[str, Any]) -> dict[str, Any] | None:
    compliance = data.get("export_compliance")
    if not compliance:
        return None
    return {
        "title": "PRC dual-use export control notice",
        "text": (
            "This specification should be handled as an export-controlled civil-security radar under the PRC Dual-Use Export Control List. "
            "The public basis is Category 6 Sensors and Lasers, item 6A108.a, issued under MOFCOM Announcement No. 51 of 2024 and effective December 1, 2024. "
            "Cyrentis can assist eligible civil customers with export-license preparation and submission support."
        ),
        "basis": "Basis: PRC Dual-Use Export Control List, Category 6 Sensors and Lasers, item 6A108.a.",
        "links": [{"label": "MOFCOM Announcement No. 51 of 2024", "url": MOFCOM_LINK}],
    }


def build_positioning_title(data: dict[str, Any]) -> str:
    focus = unique_keep_order([clean_text(item).lower() for item in (data.get("positioning", {}).get("application_focus") or [])])
    if len(focus) >= 2:
        return f"Configured for {focus[0]} and {focus[1]}."
    if len(focus) == 1:
        return f"Configured for {focus[0]}."
    return "A radar page structured for fast project evaluation and site-fit review."


def build_description(data: dict[str, Any]) -> str:
    short = sentence_case(data.get("positioning", {}).get("short") or data.get("positioning", {}).get("tagline") or "")
    instrumented = data.get("coverage", {}).get("instrumented_range_km")
    if short and meaningful(instrumented) and "km" not in short.lower():
        return f"{short.rstrip('.')} with up to {format_distance_km(instrumented)} instrumented range."
    return short or sentence_case(data.get("content", {}).get("summary"))


def build_body_paragraphs(data: dict[str, Any]) -> list[str]:
    model = clean_text(data.get("model"))
    product_name = clean_text(data.get("product_name") or model)
    band = clean_text(data.get("technical_classification", {}).get("band", {}).get("name"))
    waveform = clean_text(data.get("technical_classification", {}).get("waveform", {}).get("name"))
    architecture = clean_text(data.get("technical_classification", {}).get("scan_architecture", {}).get("name"))
    summary = clean_text(data.get("content", {}).get("summary"))
    use_cases = unique_keep_order((data.get("positioning", {}).get("application_focus") or []) + (data.get("use_cases", {}).get("secondary") or []))
    modules = data.get("platform_integration", {}).get("supported_modules") or []
    focus_text = list_join([item.lower() for item in use_cases[:3]])
    paragraph_one = f"{product_name} is positioned for {focus_text or 'civil-security monitoring'} projects where operators need {band} {waveform} sensing and a readable site-warning layer."
    paragraph_one += f" The {architecture.lower()} architecture supports structured deployment planning and downstream response coordination."

    summary_sentences = [segment.strip() for segment in re.split(r"(?<=[.!?])\s+", summary) if segment.strip()]
    paragraph_two = clean_text(" ".join(summary_sentences[:2])) or (
        f"The platform is intended to deliver stable sensing, practical target handling, and readable radar output for customers who need a deployable site-warning layer."
    )

    module_text = list_join(modules[:4])
    use_case_text = list_join([item.lower() for item in use_cases[:3]])
    paragraph_three = (
        f"In coordinated deployments, the radar can feed {module_text or 'Horizon monitoring'} workflows and support downstream cueing, verification, and response across {use_case_text or 'layered site surveillance'}."
    )

    return [sentence_case(paragraph_one), sentence_case(paragraph_two), sentence_case(paragraph_three)]


def build_front_matter(data: dict[str, Any], catalog: list[dict[str, Any]]) -> dict[str, Any]:
    model = clean_text(data["model"])
    slug = model.lower()
    description = build_description(data)
    front_matter: dict[str, Any] = {
        "title": model,
        "description": description,
        "kicker": "SRC Radar",
        "layout": "src-detail-sample",
        "slug": slug,
        "aliases": [f"/complete-products/radar/{slug}/"],
        "series_label": "SRC surveillance radar series",
        "model": model,
        "band": clean_text(data.get("technical_classification", {}).get("band", {}).get("name")),
        "system_type": clean_text(data.get("technical_classification", {}).get("waveform", {}).get("name")),
        "architecture_name": clean_text(data.get("technical_classification", {}).get("scan_architecture", {}).get("name")),
        "hero_image": resolve_ref_image(model),
        "positioning_title": build_positioning_title(data),
        "hero_stats": build_hero_stats(data),
        "feature_cards": build_feature_cards(data),
        "coverage_table": build_coverage_table(model, data),
        "technical_snapshot": build_technical_snapshot(data),
        "integration_modules": build_integration_modules(data),
        "deployment_scenarios": build_deployment_scenarios(data),
        "related_products": build_related_products(data, catalog),
    }
    compliance_notice = build_compliance_notice(data)
    if compliance_notice:
        front_matter["compliance_notice"] = compliance_notice
    return front_matter


def render_page(data: dict[str, Any], catalog: list[dict[str, Any]]) -> str:
    front_matter = build_front_matter(data, catalog)
    body = "\n\n".join(build_body_paragraphs(data))
    dumped = yaml.dump(front_matter, Dumper=NoAliasDumper, allow_unicode=True, sort_keys=False)
    return f"---\n{dumped}---\n{body}\n"


def write_page(yaml_path: Path, catalog: list[dict[str, Any]]) -> Path:
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    model = clean_text(data["model"])
    target_dir = OUTPUT_DIR / model.lower()
    target_dir.mkdir(parents=True, exist_ok=True)
    output_path = target_dir / "index.md"
    output_path.write_text(render_page(data, catalog), encoding="utf-8")
    return output_path


def remove_legacy_sources(models: list[str]) -> list[Path]:
    removed: list[Path] = []
    for model in models:
        legacy_dir = LEGACY_DIR / model.lower()
        if legacy_dir.exists():
            shutil.rmtree(legacy_dir)
            removed.append(legacy_dir)
    return removed


def collect_yaml_paths(models: list[str] | None, all_models: bool) -> list[Path]:
    if all_models or not models:
        return sorted(DOCS_DIR.glob("SRC-*.yaml"))
    paths: list[Path] = []
    for model in models:
        candidate = DOCS_DIR / f"{model.upper()}.yaml"
        if not candidate.exists():
            raise FileNotFoundError(f"Missing YAML for model: {model}")
        paths.append(candidate)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate SRC radar detail pages under content/en/sensors/src.")
    parser.add_argument("--all", action="store_true", help="Generate all SRC detail pages from docs/SRC-*.yaml.")
    parser.add_argument("--model", action="append", help="Generate one model. Repeatable.")
    parser.add_argument(
        "--remove-legacy-sources",
        action="store_true",
        help="Delete legacy content/en/complete-products/radar/src-*/ source directories after generation.",
    )
    args = parser.parse_args()

    yaml_paths = collect_yaml_paths(args.model, args.all)
    catalog = [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted(DOCS_DIR.glob("SRC-*.yaml"))]
    written: list[Path] = []
    models: list[str] = []
    for yaml_path in yaml_paths:
        written.append(write_page(yaml_path, catalog))
        models.append(yaml_path.stem)

    removed = remove_legacy_sources(models) if args.remove_legacy_sources else []

    print(f"Wrote {len(written)} SRC detail pages.")
    for path in written[:5]:
        print(f"  - {path.relative_to(ROOT)}")
    if len(written) > 5:
        print(f"  ... and {len(written) - 5} more")
    if removed:
        print(f"Removed {len(removed)} legacy source directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

