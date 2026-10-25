#!/usr/bin/env python3
"""Teste conservador: captura imagem og:image de até 3 anúncios HEERA.
Sem login, captcha bypass ou tentativa de contornar bloqueios.
Execute no PC: py tools/baixar_fotos.py
"""
import csv
import html
import json
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "imagens" / "pendentes_validacao"
REPORT = ROOT / "imagens" / "relatorio_imagens.csv"
INDEX = ROOT / "index.html"
LIMIT = 3

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metadata = {}
    def handle_starttag(self, tag, attrs):
        if tag != "meta":
            return
        a = dict(attrs)
        key = a.get("property") or a.get("name")
        if key and a.get("content"):
            self.metadata[key.lower()] = html.unescape(a["content"])

def request(url, *, max_bytes=5_000_000):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; HEERA-manual-image-check/1.0)",
        "Accept": "text/html,image/avif,image/webp,image/*,*/*;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=18) as response:
        size = response.headers.get("Content-Length")
        if size and int(size) > max_bytes:
            raise ValueError("Arquivo maior que o limite")
        return response.read(max_bytes + 1), response.headers.get("Content-Type", "")

def main():
    source = INDEX.read_text(encoding="utf-8")
    match = re.search(r"const P=(\[.*?\]);const \$=", source, flags=re.S)
    if not match:
        raise RuntimeError("Não encontrei o catálogo no index.html")
    catalog = json.loads(match.group(1))
    pending = [p for p in catalog if not p.get("image")][:LIMIT]
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for product in pending:
        pid, url = product["id"], product["url"]
        row = {"marca": product["brand"], "produto": product["name"], "id": pid, "url": url, "arquivo": "", "status": ""}
        try:
            page, content_type = request(url)
            if "html" not in content_type.lower():
                raise ValueError("Resposta da Shopee não é HTML")
            parser = MetaParser()
            parser.feed(page.decode("utf-8", errors="replace"))
            photo_url = parser.metadata.get("og:image")
            page_title = parser.metadata.get("og:title", "")
            if not photo_url or not photo_url.startswith("https://"):
                raise ValueError("Nenhuma imagem principal pública encontrada (possível bloqueio)")
            if not page_title or not any(w in page_title.lower() for w in product["brand"].lower().split()):
                raise ValueError("Título do anúncio não confirmado: revisão manual necessária")
            img, image_type = request(photo_url)
            if len(img) > 5_000_000 or not image_type.lower().startswith("image/"):
                raise ValueError("Resposta não é imagem válida")
            ext = ".jpg" if ("jpeg" in image_type or "jpg" in image_type) else ".webp" if "webp" in image_type else ".png" if "png" in image_type else ""
            if not ext:
                raise ValueError("Formato da imagem não suportado")
            path = OUTPUT / (re.sub(r"[^a-zA-Z0-9_-]", "_", str(pid)) + ext)
            path.write_bytes(img)
            row["arquivo"] = str(path.relative_to(ROOT))
            row["status"] = "BAIXADA - CONFERIR VISUALMENTE"
        except Exception as ex:
            row["status"] = "PENDENTE: " + str(ex)[:180]
        rows.append(row)
        print(f"{pid} | {row['status']}")
        time.sleep(2)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8-sig") as fp:
        writer = csv.DictWriter(fp, fieldnames=["marca", "produto", "id", "url", "arquivo", "status"], delimiter=";")
        writer.writeheader()
        writer.writerows(rows)
    print("Relatório:", REPORT)
    print("Nenhuma imagem é publicada no catálogo automaticamente.")

if __name__ == "__main__":
    main()
