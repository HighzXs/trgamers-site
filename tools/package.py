"""Gera a pasta dist/ só com os arquivos públicos do site (usado no deploy do Netlify).
Nunca publica: originals/, tools/, serve.py, readme, .bat.
"""
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

subprocess.run([sys.executable, str(ROOT / "tools" / "build.py")], check=True, cwd=ROOT)

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()

for f in ["index.html", "404.html", "robots.txt", "sitemap.xml", "favicon.ico"]:
    shutil.copy2(ROOT / f, DIST / f)
for d in ["montagem", "upgrade", "manutencao", "notebooks", "produtos", "monte-seu-pc", "sobre", "contato", "css", "js"]:
    shutil.copytree(ROOT / d, DIST / d)
shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("originals"))
print("dist/ pronto:", sum(1 for _ in DIST.rglob("*") if _.is_file()), "arquivos")

# Versão nos arquivos: quando CSS/JS mudam, o endereço muda e o navegador nunca usa cópia velha.
files = sorted(list((DIST / "css").glob("*.css")) + list((DIST / "js").glob("*.js")))
ver = hashlib.md5(b"".join(f.read_bytes() for f in files)).hexdigest()[:8]
for js in (DIST / "js").glob("*.js"):
    t = js.read_text(encoding="utf-8")
    t = re.sub(r'(from\s+"\./[\w-]+\.js)"', lambda m: m.group(1) + "?v=" + ver + '"', t)
    t = re.sub(r'(import\("\./[\w-]+\.js)"\)', lambda m: m.group(1) + "?v=" + ver + '")', t)
    js.write_text(t, encoding="utf-8")
for html in DIST.rglob("*.html"):
    t = html.read_text(encoding="utf-8")
    t = re.sub(r'((?:href|src)="/(?:css|js)/[\w-]+\.(?:css|js))"', lambda m: m.group(1) + "?v=" + ver + '"', t)
    html.write_text(t, encoding="utf-8")
print("versao dos arquivos:", ver)
