#!/bin/sh
# Prüft nach dem Release alles live. Aufruf: sh lernreise/pruefen/live.sh
# Ausgabe: je Prüfung OK oder FEHLT, am Ende GRÜN oder ROT.
B=https://janrummel.github.io
F=0
ok(){ echo "OK    $1"; }
fehlt(){ echo "FEHLT $1"; F=$((F+1)); }
hat(){ # url text beschreibung
  if curl -sL -A "Mozilla/5.0" "$1" | grep -q "$2"; then ok "$3"; else fehlt "$3 ($1)"; fi; }

# Lernreise: alle Seiten mit eigenem Titel
for p in de/ de/karte/ de/etappe-1/aufgabe-waehlen/ de/etappe-1/konto-und-daten/ de/etappe-1/erste-anfrage/ \
  de/etappe-2/anfrage-bauen/ de/etappe-2/dokument-pruefen/ de/etappe-2/in-runden/ \
  de/etappe-3/gegen-die-quelle/ de/etappe-3/websuche/ de/etappe-3/gegenlesen/ \
  de/etappe-4/daueranweisung/ de/etappe-4/projekte/ de/etappe-4/ablage-und-regeln/ de/etappe-5/ausblick-agenten/; do
  c=$(curl -s -o /dev/null -w "%{http_code}" "$B/ai-fluency/$p"); [ "$c" = 200 ] && ok "Lernreise $p" || fehlt "Lernreise $p ($c)"
done
hat "$B/ai-fluency/de/" "Kein Anbieter bezahlt uns" "Startseite ist der neue Stand"
hat "$B/ai-fluency/de/etappe-4/projekte/" "claude-5-projekt" "Etappe 4 mit Claude-Bildern"
hat "$B/ai-fluency/de/l1-first-steps/01-what-is-ai/" "Lernreise" "Alte AI-Fluency-Adresse zeigt Hinweis"
hat "$B/ai-fluency/de/uebung/uebungsangebot-kopierer.pdf" "PDF" "Übungs-PDF erreichbar"

# Hinweisseiten der alten Kurse
for r in agent-literacy github-fuer-nicht-programmierer obsidian-fuer-einsteiger ai-learning level-up-ai ai-product-thinking; do
  hat "$B/$r/" "Alle Etappen sind frei" "Hinweisseite $r"
done

# janrummel.eu
hat https://janrummel.eu/ "Alle Etappen frei" "janrummel.eu Startseite"
hat https://janrummel.eu/lehre.html "Gemini oder Claude" "janrummel.eu Angebote"
hat https://janrummel.eu/datenschutz.html "werkzeug" "janrummel.eu Datenschutz mit Werkzeugwahl"
c=$(curl -s -o /dev/null -w "%{http_code}" "https://janrummel.eu/janrummel-eu-$(date +%Y-%m-%d).zip"); [ "$c" = 404 ] && ok "Upload-Zip nicht öffentlich" || fehlt "Upload-Zip liegt öffentlich ($c)"

[ $F = 0 ] && echo "GRÜN: alles live" || { echo "ROT: $F fehlen"; exit 1; }
