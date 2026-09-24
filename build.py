"""Create a portable, static photo gallery. Standard library only."""
import json, os, re, shutil
from pathlib import Path
from urllib.parse import quote
ROOT=Path(__file__).resolve().parent
SITE=ROOT
photos=[]
metadata_path=SITE/'captions.json'
metadata=json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
for p in sorted((SITE/'photos').rglob('*'), key=lambda p:p.as_posix().casefold()):
    if p.is_symlink():
        raise ValueError('Photo symlinks are not supported')
    if p.is_file() and p.suffix.lower() in {'.jpg','.jpeg','.png','.webp','.avif','.gif'}:
        rel=p.relative_to(SITE).as_posix()
        name=p.relative_to(SITE/'photos').as_posix()
        photos.append({'src':'./'+quote(rel,safe='/'),'title':str(metadata.get(name,p.stem))})
repo=os.environ.get('GITHUB_REPOSITORY','')
manage=f'https://github.com/{repo}/tree/main/photos' if re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo) else ''
(SITE/'photos.js').write_text('window.GALLERY_PHOTOS = '+json.dumps(photos,ensure_ascii=True)+';\nwindow.GALLERY_MANAGE_URL = '+json.dumps(manage)+';\n',encoding='utf-8')
out=ROOT/'_site'
if out.exists():shutil.rmtree(out)
out.mkdir()
for name in ['index.html','style.css','gallery.js','photos.js','favicon.svg']:
    shutil.copy2(SITE/name,out/name)
for p in photos:
    from urllib.parse import unquote
    rel=unquote(p['src'][2:]); dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SITE/rel,dest)
(out/'.nojekyll').touch()
print(f'Built {len(photos)} photos into _site/')
