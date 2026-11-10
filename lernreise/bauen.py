#!/usr/bin/env python3
"""Baut die Lernreise "Erst das Problem, dann die KI" als statische Seiten nach site/.

Quellen: lernreise/quellen/<sprache>/*.html sind die Einheiten so, wie sie geschrieben
und als Vorschau geprüft wurden (ohne <head>-Gerüst). Dieses Skript ergänzt nur
Mechanik: HTML-Gerüst, eigene Schriften statt Google Fonts, Kopfleiste, Fuß mit
Rückmeldeweg, Zählung (GoatCounter), echte Links statt Vorschau-Links, Weiterleitung
der alten Kursadressen. Inhalt wird nicht verändert.

Aufruf: python3 lernreise/bauen.py   (Ergebnis in site/, prüft sich am Ende selbst)
"""
import html
import pathlib
import re
import shutil
import sys

WURZEL = pathlib.Path(__file__).resolve().parent
REPO = WURZEL.parent
ZIEL = REPO / "site"
BASIS_URL = "https://janrummel.github.io/ai-fluency/"
STAND = "10.11.2026"
NAME = "Erst das Problem, dann die KI"

# Quelle, Zielpfad unter de/, Vorschau-ID (claude.ai/artifact/<id>), Kurzname für die Kopfleiste
SEITEN_DE = [
    ("start.html", "", "lr:start", None),
    ("karte.html", "karte/", "C2uR6nxrPKWBmGXfrR9gdE", "Bausteinkarte"),
    ("e1-aufgabe-waehlen.html", "etappe-1/aufgabe-waehlen/", "Scyy67sGaFb3g5n6yepHRh", "Etappe 1 · Einheit 1"),
    ("e1-konto-und-daten.html", "etappe-1/konto-und-daten/", "5cK68G61BWehLw6bxP5Z6j", "Etappe 1 · Einheit 2"),
    ("e1-erste-anfrage.html", "etappe-1/erste-anfrage/", "Vn6TnYtQievpv3kZUJAgjs", "Etappe 1 · Einheit 3"),
    ("e2-anfrage-bauen.html", "etappe-2/anfrage-bauen/", "UJyTgyB68HE5AcWNbgsnVt", "Etappe 2 · Einheit 1"),
    ("e2-dokument-pruefen.html", "etappe-2/dokument-pruefen/", "M835sRMTgTn6hWcvfv5ZqK", "Etappe 2 · Einheit 2"),
    ("e2-in-runden.html", "etappe-2/in-runden/", "MgrJBfUYMzMaBE6WigSaST", "Etappe 2 · Einheit 3"),
]

LEISTE_CSS = """
.lr-leiste{border-bottom:1px solid var(--linie,#DAD8D0);background:var(--papier,#FBFAF6)}
.lr-leiste-innen{max-width:var(--lr-breite,760px);margin:0 auto;padding-block:10px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-wrap:wrap;align-items:center;gap:4px 18px;font-family:var(--f-etikett,'IBM Plex Mono',ui-monospace,Menlo,monospace);font-size:12px;letter-spacing:.06em;text-transform:uppercase}
.lr-leiste a{color:var(--tinte,#17181A);text-decoration:none;display:inline-flex;align-items:center;min-height:36px}
.lr-leiste a:hover{text-decoration:underline;text-decoration-color:var(--rot,#C4472B)}
.lr-leiste .lr-name{font-family:var(--f-titel,'Newsreader',Georgia,serif);font-size:17px;letter-spacing:0;text-transform:none;margin-right:auto}
.lr-leiste .lr-hier{color:var(--grau,#6A6A66)}
.lr-fuss{border-top:1px solid var(--linie,#DAD8D0);background:var(--sand,#EFE9DD);color:var(--tinte,#17181A);font-family:var(--f-text,'IBM Plex Sans',system-ui,sans-serif);font-size:15px;line-height:1.55}
.lr-fuss-innen{max-width:var(--lr-breite,760px);margin:0 auto;padding-block:26px 34px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:12px}
.lr-fuss b{font-weight:500}
.lr-fuss a{color:inherit;text-underline-offset:3px;text-decoration-color:var(--rot,#C4472B)}
.lr-fuss .lr-klein{font-family:var(--f-etikett,'IBM Plex Mono',ui-monospace,Menlo,monospace);font-size:11.5px;letter-spacing:.05em;color:var(--grau,#6A6A66);display:flex;flex-wrap:wrap;gap:4px 16px}
.lr-fuss .lr-klein a{display:inline-flex;align-items:center;min-height:32px}
"""


def tiefe_prefix(zielpfad: str, sprache: str) -> str:
    """Relativer Weg von der Seite zur Site-Wurzel (site/)."""
    stufen = 1 + zielpfad.count("/")  # de/ + Unterordner
    return "../" * stufen


def leiste(prefix: str, sprache: str, kurz: str | None) -> str:
    start = f"{prefix}{sprache}/"
    teile = [f'<a class="lr-name" href="{start}">{NAME}</a>']
    if kurz:
        teile.append(f'<span class="lr-hier">{html.escape(kurz)}</span>')
    teile.append(f'<a href="{start}">Start</a>')
    teile.append(f'<a href="{start}karte/">Karte</a>')
    return ('<nav class="lr-leiste" aria-label="Lernreise">'
            f'<div class="lr-leiste-innen">{"".join(teile)}</div></nav>')


def fuss() -> str:
    return (
        '<div class="lr-fuss" role="contentinfo"><div class="lr-fuss-innen">'
        '<p><b>Etwas unklar, falsch oder veraltet?</b> Schreib mir einen Satz an '
        '<a href="mailto:kontakt@janrummel.eu?subject=Lernreise">kontakt@janrummel.eu</a>. '
        'Jede Rückmeldung wird gelesen.</p>'
        f'<p>Eine Lernreise von <a href="https://janrummel.eu/">Jan Rummel</a>. Stand {STAND}. '
        'Texte und Bilder stehen unter <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.de">CC BY-SA 4.0</a>: '
        'teilen und anpassen erlaubt, mit Namensnennung und unter gleicher Lizenz.</p>'
        '<div class="lr-klein">'
        '<a href="https://janrummel.eu/impressum.html">Impressum</a>'
        '<a href="https://janrummel.eu/datenschutz.html">Datenschutz</a>'
        '<a href="https://github.com/janrummel/ai-fluency">Quelltext</a>'
        '</div></div></div>'
    )


def kopf(titel: str, beschreibung: str | None, prefix: str, url: str, sprache: str) -> str:
    zeilen = [
        "<!doctype html>",
        f'<html lang="{sprache}">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
        f"<title>{html.escape(titel)}</title>",
    ]
    if beschreibung:
        zeilen.append(f'<meta name="description" content="{html.escape(beschreibung)}">')
    zeilen += [
        f'<link rel="canonical" href="{url}">',
        f'<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">',
        f'<link rel="stylesheet" href="{prefix}assets/schriften.css">',
        f'<script data-goatcounter="https://janrummel.goatcounter.com/count" async src="{prefix}assets/count.js"></script>',
        f"<style>{LEISTE_CSS}</style>",
    ]
    return "\n".join(zeilen)


def seite_bauen(quelle: pathlib.Path, zielpfad: str, kurz: str | None, sprache: str, links: dict) -> str:
    s = quelle.read_text(encoding="utf-8")
    m = re.search(r"<title>(.*?)</title>\s*", s, re.S)
    if not m:
        raise SystemExit(f"{quelle.name}: kein <title>")
    titel_roh = html.unescape(m.group(1).strip())
    s = s.replace(m.group(0), "", 1)
    beschreibung = None
    m = re.search(r'<meta name="description" content="([^"]*)">\s*', s)
    if m:
        beschreibung = html.unescape(m.group(1))
        s = s.replace(m.group(0), "", 1)
    # Vorschau-Reste und Google Fonts entfernen
    s = re.sub(r'<meta name="claude:[^>]*>\s*', "", s)
    s = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", s)
    s = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>\s*', "", s)
    prefix = tiefe_prefix(zielpfad, sprache)
    # Links auf andere Einheiten
    def ersetze(mm):
        ziel = links.get(mm.group(1))
        if ziel is None:
            raise SystemExit(f"{quelle.name}: unbekannter Link {mm.group(1)}")
        return f'href="{prefix}{sprache}/{ziel}"'
    s = re.sub(r'href="https://claude\.ai/artifact/([A-Za-z0-9]+)"', ersetze, s)
    s = re.sub(r'href="(lr:[a-z0-9-]+)"', ersetze, s)
    # Bilder und Übungsdatei liegen einmal je Sprache
    s = s.replace('src="bilder/', f'src="{prefix}{sprache}/bilder/')
    s = s.replace('href="uebungsangebot-kopierer.pdf"', f'href="{prefix}{sprache}/uebung/uebungsangebot-kopierer.pdf"')

    # Kopf und Körper trennen: alles bis zum ersten Inhaltselement gehört in den <head>
    m = re.search(r"<(div|main|header|section)\b", s)
    kopfteil, koerper = s[: m.start()], s[m.start():]
    titel = titel_roh if not kurz else f"{titel_roh} · {NAME}"
    mb = re.search(r"\.seite\{max-width:(\d+)px", kopfteil)
    breite = f'<style>:root{{--lr-breite:{mb.group(1)}px}}</style>' if mb else ""
    url = f"{BASIS_URL}{sprache}/{zielpfad}"
    return (
        kopf(titel, beschreibung, prefix, url, sprache) + "\n" + kopfteil.strip() + breite + "\n</head>\n<body>\n"
        + leiste(prefix, sprache, kurz) + "\n" + koerper.strip() + "\n" + fuss() + "\n</body>\n</html>\n"
    )


WEITERLEITUNG_404 = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Seite nicht gefunden · Erst das Problem, dann die KI</title>
<link rel="stylesheet" href="/ai-fluency/assets/schriften.css">
<style>
:root{--papier:#FBFAF6;--tinte:#17181A;--grau:#6A6A66;--linie:#DAD8D0;--rot:#C4472B;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--papier:#18191B;--tinte:#ECE9E1;--grau:#A8A69F;--linie:#3A3A37;--rot:#E4704F;color-scheme:dark}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--papier);color:var(--tinte);font:17px/1.6 'IBM Plex Sans',system-ui,sans-serif;min-height:100vh;display:grid;place-items:center;padding-block:40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
main{max-width:34rem;display:grid;gap:16px}
.etikett{font:12px/1.4 'IBM Plex Mono',ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--rot)}
h1{font:400 clamp(28px,6vw,38px)/1.15 'Newsreader',Georgia,serif}
p{color:var(--grau)}
a{color:var(--tinte);text-decoration-color:var(--rot);text-underline-offset:3px}
.knopf{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border:1px solid var(--rot);color:var(--rot);text-decoration:none;font:13px 'IBM Plex Mono',ui-monospace,Menlo,monospace;letter-spacing:.06em;text-transform:uppercase}
.en{border-top:1px solid var(--linie);padding-top:14px;font-size:15px}
</style>
</head>
<body>
<main>
  <span class="etikett" id="etikett">Seite nicht gefunden</span>
  <h1 id="titel">Diese Seite gibt es hier nicht.</h1>
  <p id="text">Vielleicht hat sich die Adresse geändert. Die Lernreise beginnt auf der Startseite.</p>
  <p><a class="knopf" href="/ai-fluency/de/">Zum Start der Lernreise</a></p>
  <p class="en" lang="en">Page not found. The course "AI Fluency" has become the learning journey <i>Erst das Problem, dann die KI</i> (German first, English later). <a href="/ai-fluency/en/">English page</a></p>
</main>
<script>
(function(){
  var p=location.pathname;
  if(/\\/ai-fluency\\/(de|en)\\/(l[1-4]-|start\\/|reference\\/)/.test(p)){
    document.getElementById('etikett').textContent='AI Fluency ist jetzt die Lernreise';
    document.getElementById('titel').textContent='Der Kurs AI Fluency ist in der neuen Lernreise aufgegangen.';
    document.getElementById('text').textContent='Die alten Lektionen gibt es nicht mehr einzeln. Ihr Stoff steckt jetzt in den Etappen der Lernreise „Erst das Problem, dann die KI“: kürzer, mit echten Übungen.';
  }
})();
</script>
</body>
</html>
"""

WURZEL_INDEX = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Erst das Problem, dann die KI</title>
<link rel="canonical" href="https://janrummel.github.io/ai-fluency/de/">
<meta http-equiv="refresh" content="0; url=de/">
</head>
<body>
<p><a href="de/">Weiter zur Lernreise „Erst das Problem, dann die KI“</a> · <a href="en/">English</a></p>
</body>
</html>
"""

EN_INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>First the problem, then the AI</title>
<link rel="stylesheet" href="../assets/schriften.css">
<script data-goatcounter="https://janrummel.goatcounter.com/count" async src="../assets/count.js"></script>
<style>
:root{--papier:#FBFAF6;--tinte:#17181A;--grau:#6A6A66;--linie:#DAD8D0;--rot:#C4472B;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--papier:#18191B;--tinte:#ECE9E1;--grau:#A8A69F;--linie:#3A3A37;--rot:#E4704F;color-scheme:dark}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--papier);color:var(--tinte);font:17px/1.6 'IBM Plex Sans',system-ui,sans-serif;min-height:100vh;display:grid;place-items:center;padding-block:40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
main{max-width:34rem;display:grid;gap:16px}
.etikett{font:12px/1.4 'IBM Plex Mono',ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--rot)}
h1{font:400 clamp(28px,6vw,38px)/1.15 'Newsreader',Georgia,serif}
p{color:var(--grau)}
a{color:var(--tinte);text-decoration-color:var(--rot);text-underline-offset:3px}
</style>
</head>
<body>
<main>
  <span class="etikett">English version · coming later</span>
  <h1>First the problem, then the AI.</h1>
  <p>A free learning journey for working with ChatGPT, Copilot and Gemini at the office: clarify the task, ask well, check the answer. The German version comes first. The English one follows.</p>
  <p><a href="../de/">Go to the German version</a> · Questions: kontakt@janrummel.eu</p>
</main>
</body>
</html>
"""

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" fill="#17181A"/>'
           '<path d="M8 22h16" stroke="#C4472B" stroke-width="3"/>'
           '<circle cx="16" cy="13" r="5" fill="none" stroke="#FBFAF6" stroke-width="2.5"/></svg>')


def pruefen(ziel: pathlib.Path) -> list[str]:
    fehler = []
    for f in ziel.rglob("*.html"):
        t = f.read_text(encoding="utf-8")
        rel = f.relative_to(ziel)
        for muster, was in [("claude.ai/artifact", "Vorschau-Link"), ("fonts.googleapis", "Google Fonts"),
                            ("fonts.gstatic", "Google Fonts"), ("(folgt)", "Platzhalter (folgt)"),
                            ("Muster, Entwurf", "Entwurfsvermerk"), ('href="lr:', "unaufgelöster Link")]:
            if muster in t:
                fehler.append(f"{rel}: {was}")
        if not t.startswith("<!doctype html>"):
            fehler.append(f"{rel}: kein doctype")
        # relative Verweise müssen existieren
        for ref in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', t):
            if ref.startswith("/") or ref.startswith("mailto"):
                continue
            ziel_datei = (f.parent / ref).resolve()
            if ref.endswith("/"):
                ziel_datei = ziel_datei / "index.html"
            if not ziel_datei.exists():
                fehler.append(f"{rel}: toter Verweis {ref}")
    return fehler


def main():
    if ZIEL.exists():
        shutil.rmtree(ZIEL)
    (ZIEL / "de").mkdir(parents=True)
    links = {sid: pfad for _, pfad, sid, _ in SEITEN_DE}
    for datei, pfad, _, kurz in SEITEN_DE:
        out = ZIEL / "de" / pfad / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(seite_bauen(WURZEL / "quellen/de" / datei, pfad, kurz, "de", links), encoding="utf-8")
    for unterordner in ("bilder", "uebung"):
        shutil.copytree(WURZEL / "quellen/de" / unterordner, ZIEL / "de" / unterordner)
    shutil.copytree(WURZEL / "statisch/assets", ZIEL / "assets")
    (ZIEL / "en").mkdir()
    (ZIEL / "en/index.html").write_text(EN_INDEX, encoding="utf-8")
    (ZIEL / "index.html").write_text(WURZEL_INDEX, encoding="utf-8")
    (ZIEL / "404.html").write_text(WEITERLEITUNG_404, encoding="utf-8")
    (ZIEL / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (ZIEL / ".nojekyll").write_text("", encoding="utf-8")
    urls = [f"{BASIS_URL}de/{p}" for _, p, _, _ in SEITEN_DE]
    (ZIEL / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ZIEL / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASIS_URL}sitemap.xml\n", encoding="utf-8")
    fehler = pruefen(ZIEL)
    n = len(list(ZIEL.rglob("*.html")))
    if fehler:
        print("\n".join(fehler))
        sys.exit(f"{len(fehler)} Fehler in {n} Seiten")
    print(f"gebaut: {n} Seiten in {ZIEL.relative_to(REPO)}/, Prüfung ohne Befund")


if __name__ == "__main__":
    main()
