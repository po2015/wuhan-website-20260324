import zipfile, re
from pathlib import Path
base = Path(r'e:\Cyrentis\site\source_material\soc\new')
for path in base.glob('*.docx'):
    print(f'\n=== {path.name} ===')
    with zipfile.ZipFile(path) as zf:
        xml = zf.read('word/document.xml').decode('utf-8', errors='ignore')
        names = [n for n in zf.namelist() if n.startswith('word/media/')]
    texts = [re.sub(r'<.*?>', '', t) for t in re.findall(r'<w:p[\s\S]*?</w:p>', xml)]
    shown = 0
    for t in texts:
        t = re.sub(r'\s+', ' ', t).strip()
        if t:
            print(t)
            shown += 1
        if shown >= 120:
            break
    print('MEDIA', len(names), names[:12])
