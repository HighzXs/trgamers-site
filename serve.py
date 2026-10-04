"""Servidor de desenvolvimento com recarga automática.
Uso:  python serve.py   ->  http://localhost:8000
- Sem cache (sempre serve o arquivo mais novo).
- Recarrega a aba sozinha quando HTML/CSS/JS/imagens mudam.
- Se tools/build.py mudar, regera as páginas antes de recarregar.
"""
import subprocess
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = 8000
BUILD = ROOT / "tools" / "build.py"
EXTS = {".html", ".css", ".js", ".json", ".webp", ".jpg", ".png", ".svg"}
SKIP = {"originals", ".git", "node_modules", "tools"}

RELOAD_JS = b"""<script>(function(){var v=null;setInterval(function(){fetch('/__v',{cache:'no-store'}).then(function(r){return r.text()}).then(function(t){if(v===null)v=t;else if(t!==v)location.reload()}).catch(function(){})},700)})()</script>"""

state = {"build": 0.0}


def snapshot():
    """Maior mtime dos arquivos do site; regera páginas se build.py mudou."""
    if BUILD.exists() and BUILD.stat().st_mtime != state["build"]:
        first = state["build"] == 0.0
        state["build"] = BUILD.stat().st_mtime
        if not first:
            subprocess.run([sys.executable, str(BUILD)], cwd=ROOT)
    latest = 0.0
    for p in ROOT.rglob("*"):
        if p.suffix in EXTS and not SKIP.intersection(p.relative_to(ROOT).parts):
            latest = max(latest, p.stat().st_mtime)
    return str(latest)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/__v":
            body = snapshot().encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        fs = Path(self.translate_path(path))
        if fs.is_dir():
            fs = fs / "index.html"
        if fs.suffix == ".html" and fs.exists():
            html = fs.read_bytes()
            html = html.replace(b"</body>", RELOAD_JS + b"</body>") if b"</body>" in html else html + RELOAD_JS
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
            return
        super().do_GET()

    def log_message(self, fmt, *args):
        if "/__v" not in str(args[0]):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    snapshot()
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"Rodando em {url}  (Ctrl+C para parar)")
    webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrado.")
