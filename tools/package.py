"""Gera a pasta dist/ só com os arquivos públicos do site (usado no deploy do Netlify).
Nunca publica: originals/, tools/, serve.py, readme, .bat.
"""
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

for f in ["index.html", "404.html", "robots.txt", "sitemap.xml"]:
    shutil.copy2(ROOT / f, DIST / f)
for d in ["montagem", "upgrade", "manutencao", "notebooks", "produtos", "monte-seu-pc", "sobre", "contato", "css", "js"]:
    shutil.copytree(ROOT / d, DIST / d)
shutil.copytree(ROOT / "assets", DIST / "assets", ignore=shutil.ignore_patterns("originals"))
print("dist/ pronto:", sum(1 for _ in DIST.rglob("*") if _.is_file()), "arquivos")
