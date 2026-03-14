# Research: System Prompt Design Best Practices

**Fuer:** AI Fluency L3 Modul
**Datum:** 2026-03-14
**Quellen:** Anthropic Docs, OpenAI Docs, Claude Code Docs, Praxis-Guides

---

## 1. Was einen guten System Prompt ausmacht

### Die goldene Regel (Anthropic)

> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."

Die Kernmetapher: Ein LLM ist wie ein brillanter neuer Mitarbeiter, der keinen Kontext zu deinen Normen und Workflows hat. Je praeziser du erklaerst was du willst, desto besser das Ergebnis.

### Anatomie eines effektiven System Prompts

Ein guter System Prompt besteht aus diesen Bausteinen — nicht alle sind immer noetig:

| Baustein | Zweck | Beispiel |
|----------|-------|---------|
| **Rolle** | Fokussiert Verhalten und Ton | "Du bist ein erfahrener Strategieberater fuer mittelstaendische Unternehmen." |
| **Kontext** | Erklaert das WARUM hinter Regeln | "Die Antwort wird laut vorgelesen — keine Ellipsen verwenden, da die Text-to-Speech-Engine sie nicht aussprechen kann." |
| **Aufgabenbeschreibung** | Was konkret getan werden soll | "Analysiere Quartalsberichte und identifiziere strategische Vorteile." |
| **Formatvorgaben** | Wie der Output aussehen soll | "Antworte in 3-5 Bullet Points, maximal 2 Saetze pro Punkt." |
| **Constraints** | Grenzen und Einschraenkungen | "Verwende nur Informationen aus den bereitgestellten Dokumenten." |
| **Beispiele** | Konkrete Input/Output-Paare | 3-5 diverse Beispiele, die Edge Cases abdecken |
| **Tonalitaet** | Sprachstil und Ansprache | "Professionell aber zugaenglich, Du-Ansprache." |

### Strukturierung mit XML Tags (Anthropic Best Practice)

XML Tags helfen dem Modell, komplexe Prompts eindeutig zu parsen — besonders wenn Instruktionen, Kontext, Beispiele und variable Inputs gemischt werden.

```xml
<role>
Du bist ein Senior Data Analyst...
</role>

<instructions>
1. Analysiere die bereitgestellten Daten
2. Identifiziere die drei wichtigsten Trends
</instructions>

<format>
Antworte in Fliesstext, keine Bullet Points.
</format>

<examples>
<example>
Input: Quartalsbericht Q3...
Output: Die Analyse zeigt...
</example>
</examples>
```

Best Practices fuer XML Tags:
- Konsistente, beschreibende Tag-Namen verwenden
- Tags verschachteln wenn Inhalte eine natuerliche Hierarchie haben
- Beispiele in `<example>` Tags wrappen, um sie von Instruktionen zu trennen

### Positiv statt negativ formulieren (Anthropic)

Statt zu sagen was das Modell NICHT tun soll, beschreibe was es stattdessen tun soll:

| Weniger effektiv | Effektiver |
|------------------|------------|
| "Verwende kein Markdown" | "Antworte in fliessendem Prosatext mit Absaetzen." |
| "Keine langen Antworten" | "Antworte in maximal 3 Saetzen pro Punkt." |
| "Keine Annahmen machen" | "Frage nach, wenn Informationen fehlen." |

---

## 2. Drei konkrete Beispiele gut gestalteter System Prompts

### Beispiel A: Schreibassistent fuer Fachtexte

```
<role>
Du bist ein erfahrener Fachredakteur fuer technische Themen. Du schreibst
fuer ein Publikum mit solidem Grundwissen, aber ohne Spezialisierung.
</role>

<style>
- Professionell aber zugaenglich
- Aktive Formulierungen bevorzugen
- Fachbegriffe beim ersten Auftreten kurz erklaeren
- Deutsch mit englischen Fachbegriffen wo branchenueblich
</style>

<format>
- Fliesstext mit klarer Absatzstruktur
- Zwischenueberschriften nur bei Texten ueber 500 Woerter
- Keine Bullet-Listen im Fliesstext — Aufzaehlungen in Saetze einbauen
</format>

<constraints>
- Behauptungen mit Quellenhinweisen stuetzen
- Bei Unsicherheit explizit kennzeichnen: "Hier bin ich nicht sicher, aber..."
- Keine Marketing-Sprache oder Superlative ohne Beleg
</constraints>

<example>
Input: Schreibe einen Absatz ueber die Vorteile von RAG.
Output: Retrieval Augmented Generation (RAG) verbindet die Staerken
grosser Sprachmodelle mit aktuellen, externen Wissensquellen. Statt sich
ausschliesslich auf Trainingsdaten zu stuetzen, durchsucht das System bei
jeder Anfrage relevante Dokumente und integriert diese Informationen in
die Antwort. Das reduziert Halluzinationen messbar — Studien zeigen eine
Reduktion faktischer Fehler um 30-50% gegenueber reinem Prompting.
</example>
```

**Warum das funktioniert:**
- Klare Rolle mit Zielgruppen-Definition
- Positiv formulierte Stilregeln
- Konkretes Beispiel zeigt den gewuenschten Output
- Ehrlichkeits-Constraint ("bei Unsicherheit kennzeichnen")

### Beispiel B: Datenanalyse-Assistent

```
<role>
Du bist ein analytischer Sparringspartner fuer Geschaeftsdaten. Du hilfst
mir, Muster in Daten zu erkennen und fundierte Entscheidungen zu treffen.
</role>

<workflow>
Bei jeder Analyse gehst du so vor:
1. Zusammenfassung: Was zeigen die Daten auf einen Blick? (2-3 Saetze)
2. Kernerkenntnisse: Die 3 wichtigsten Muster oder Auffaelligkeiten
3. Kontext: Was koennte die Daten erklaeren? Welche externen Faktoren?
4. Handlungsempfehlung: Was wuerde ich basierend darauf tun?
5. Offene Fragen: Welche Daten fehlen fuer eine vollstaendige Bewertung?
</workflow>

<constraints>
- Korrelation nie als Kausalitaet darstellen
- Bei Prozentwerten immer die Absolutzahlen mit angeben
- Unsicherheit quantifizieren wenn moeglich ("mit Vorbehalt, da n=12")
- Keine Empfehlungen ohne datenbasierte Begruendung
</constraints>

<my_context>
Ich bin Product Manager bei einem B2B SaaS-Unternehmen mit 200 Kunden.
Unsere wichtigsten Metriken: MRR, Churn Rate, NPS, Feature Adoption.
</my_context>
```

**Warum das funktioniert:**
- Strukturierter Workflow mit numerierten Schritten
- Harte analytische Regeln (Korrelation vs. Kausalitaet)
- Persoenlicher Kontext macht Empfehlungen relevant
- "Offene Fragen" verhindert uebermaessige Sicherheit

### Beispiel C: Kundensupport-Helfer

```
<role>
Du hilfst mir, Kundenanfragen professionell und empathisch zu beantworten.
Unser Unternehmen bietet Projektmanagement-Software fuer Teams an.
</role>

<tone>
- Freundlich und loesungsorientiert
- Klar und direkt — keine Floskeln wie "Gerne helfe ich Ihnen"
- Empathie zeigen ohne zu uebertreiben
- Siezen, ausser der Kunde duzt zuerst
</tone>

<workflow>
1. Problem in eigenen Worten zusammenfassen (zeigt Verstaendnis)
2. Loesung oder naechsten Schritt vorschlagen
3. Fragen ob das weiterhilft, oder ob ich anders helfen kann
</workflow>

<escalation>
Wenn du dir nicht sicher bist oder das Problem technisch ist:
- Sage ehrlich: "Das muss ich intern klaeren."
- Biete konkreten Zeitrahmen: "Ich melde mich bis [Zeitpunkt] zurueck."
- Erfinde KEINE Loesungen fuer technische Probleme die du nicht kennst.
</escalation>

<examples>
<example>
Kundenanfrage: "Eure Software synchronisiert seit gestern nicht mehr!"
Antwort: "Das klingt frustrierend — eine Synchronisierung die nicht
laeuft, blockiert natuerlich die Arbeit. Koennten Sie mir sagen, welche
Integration betroffen ist (Slack, Jira, oder eine andere)? Dann kann ich
gezielt pruefen, ob es ein bekanntes Problem gibt oder ob wir gemeinsam
eine Loesung finden."
</example>
</examples>
```

**Warum das funktioniert:**
- Tone-Guidance ist spezifisch ("keine Floskeln wie...")
- Eskalations-Regeln verhindern Halluzinationen bei technischen Fragen
- Das Beispiel zeigt Empathie + konkrete naechste Schritte

---

## 3. Anti-Patterns: Haeufige Fehler im System Prompt Design

### Anti-Pattern 1: Vage Instruktionen

| Problem | Besser |
|---------|--------|
| "Sei hilfreich" | "Beantworte Fragen in 2-3 Saetzen mit einem konkreten Beispiel." |
| "Formatiere gut" | "Verwende Fliesstext mit Absaetzen. Bullet Points nur fuer Listen mit 4+ Elementen." |
| "Sei professionell" | "Verwende Fachsprache wo noetig, erklaere Abkuerzungen beim ersten Auftreten." |

**Warum problematisch:** Das Modell interpretiert vage Begriffe nach eigenem Ermessen — und das variiert zwischen Anfragen.

### Anti-Pattern 2: Widerspruechliche Regeln

```
# Schlecht — widerspricht sich:
"Halte dich immer kurz."
"Erklaere jeden Punkt ausfuehrlich mit Beispielen."
```

**Loesung:** Regeln priorisieren oder kontextabhaengig machen: "Standardmaessig kurz (2-3 Saetze). Bei technischen Erklaerungen ausfuehrlicher mit Beispiel."

### Anti-Pattern 3: Ausschliesslich Verbote

```
# Schlecht — sagt nur was NICHT getan werden soll:
"Verwende KEIN Markdown."
"Keine langen Saetze."
"Halluziniere NICHT."
```

**Besser:** Positiv formulieren was stattdessen gewuenscht ist. Anthropic empfiehlt explizit: "Tell Claude what to do instead of what not to do."

### Anti-Pattern 4: Ueberladenene Prompts

System Prompts mit 500+ Zeilen fuehren zu:
- Hohem Token-Verbrauch bei JEDER Anfrage
- Sinkender Befolgungsrate (je laenger, desto mehr wird ignoriert)
- Widerspruechen zwischen Regeln

**Anthropic-Empfehlung:** Unter 200 Zeilen bleiben. Fuer komplexere Setups: Aufteilen in modulare Dateien.

### Anti-Pattern 5: ALL-CAPS Dringlichkeit

```
# Schlecht:
"CRITICAL: You MUST ALWAYS use this tool!!!"
"IMPORTANT: NEVER forget to..."
```

**Anthropic warnt explizit:** Neuere Modelle reagieren staerker auf den System Prompt. Aggressive Sprache fuehrt zu Ueberreaktionen. Normales Prompting ("Use this tool when...") reicht aus.

### Anti-Pattern 6: Kontext ohne Begruendung

```
# Schlecht:
"Verwende NIEMALS Ellipsen."

# Besser (Anthropic-Beispiel):
"Die Antwort wird von einer Text-to-Speech-Engine vorgelesen.
Verwende keine Ellipsen, da die Engine sie nicht aussprechen kann."
```

**Warum:** Das Modell kann von der Begruendung generalisieren und aehnliche Probleme selbststaendig vermeiden.

---

## 4. Persistent Context Strategies: Kontext der mit der Zeit besser wird

### Das Zwei-Schichten-Modell (Claude Code / Custom Instructions)

Moderne AI-Systeme unterscheiden zwei Arten von persistentem Kontext:

| Schicht | Wer schreibt | Was es enthaelt | Beispiel |
|---------|-------------|-----------------|---------|
| **Nutzer-definiert** | Du | Regeln, Standards, Praeferenzen | CLAUDE.md, Custom Instructions, System Prompts |
| **Auto-gelernt** | Das System | Beobachtete Muster, Korrekturen | Auto Memory, Learned Preferences |

### Strategie 1: Statische Instruktionen — "Explain your job once"

Kernidee: Alles was sich selten aendert, gehoert in persistente Instruktionen.

**Was reingehoert:**
- Deine Rolle / dein Arbeitskontext
- Bevorzugter Output-Stil (Laenge, Format, Tonalitaet)
- Fachliche Constraints ("Korrelation ist keine Kausalitaet")
- Haeufige Workflows und Ablaeufe
- Fachbegriffe und deren Verwendung

**Strukturierungsempfehlung:**
```
# Wer ich bin
Product Manager, B2B SaaS, 200 Kunden

# Wie ich arbeite
- Erst Problem verstehen, dann loesen
- Daten vor Meinungen
- Kurze Antworten, ausser ich frage nach Details

# Output-Praeferenzen
- Deutsch mit englischen Fachbegriffen
- Fliesstext statt Bullet-Listen
- Bei Unsicherheit: sagen, nicht raten

# Mein Kontext
- Wichtigste Metriken: MRR, Churn, NPS
- Tech Stack: React, Node.js, PostgreSQL
- Team: 8 Leute, remote
```

### Strategie 2: Auto Memory — "Context that compounds"

Aus der Claude Code Dokumentation: Auto Memory laesst das System Wissen ueber Sessions hinweg akkumulieren, ohne dass du etwas schreiben musst. Das System entscheidet selbst, was sich zu merken lohnt.

**Was Auto Memory typischerweise lernt:**
- Build-Befehle und Projekt-Setup
- Debugging-Muster und Loesungswege
- Code-Stil-Praeferenzen aus Korrekturen
- Architektur-Entscheidungen

**Analogie fuer Knowledge Worker:** Wie ein Assistent, der sich Notizen macht. Beim zehnten Mal fragst du nicht mehr "Formatiere bitte als Tabelle" — das System weiss es bereits.

### Strategie 3: Modularer Aufbau mit Rules

Fuer komplexere Setups — Instruktionen aufteilen nach Thema:

```
Meine Instruktionen/
├── core.md              # Kernregeln (immer geladen)
├── writing-style.md     # Schreibstil (immer geladen)
├── data-analysis.md     # Nur bei Datenarbeit
├── customer-comms.md    # Nur bei Kundenkommunikation
└── presentations.md     # Nur bei Praesentationen
```

**Vorteil:** Nicht alles wird bei jeder Anfrage geladen. Kontext-effizient und keine Widersprueche zwischen unabhaengigen Bereichen.

### Strategie 4: Iteratives Verfeinern

Der beste System Prompt entsteht nicht beim ersten Versuch:

1. **Starte minimal** — Rolle + 3-5 Kernregeln
2. **Beobachte** — Wo weicht der Output ab?
3. **Korrigiere gezielt** — Eine Regel pro Problem hinzufuegen
4. **Pruefe auf Widersprueche** — Konfligierende Regeln finden und aufloesen
5. **Bereinige** — Veraltete oder redundante Regeln entfernen

---

## 5. Wann Persistent Context hilft — und wann nicht

### Persistent Context HILFT bei:

| Situation | Warum |
|-----------|-------|
| **Wiederkehrende Aufgaben** | Gleicher Stil, gleiches Format, gleiches Qualitaetsniveau — jedes Mal |
| **Komplexer Fachkontext** | Branchenspezifisches Wissen muss nicht jedes Mal neu erklaert werden |
| **Team-Konsistenz** | Alle bekommen den gleichen Standard-Output |
| **Lange Projekte** | Kontext geht nicht verloren wenn Sessions enden |
| **Persoenliche Praeferenzen** | "Ich will immer Tabellen statt Bullet Points" — einmal sagen, immer bekommen |
| **Quality Standards** | Analytische Constraints ("Quelle angeben", "Unsicherheit kennzeichnen") werden nie vergessen |

### Persistent Context SCHADET bei:

| Situation | Warum |
|-----------|-------|
| **Einfache One-Off Fragen** | "Was ist die Hauptstadt von Frankreich?" braucht keinen Kontext |
| **Schnell wechselnde Anforderungen** | Wenn sich Regeln woechentlich aendern, wird Pflege zum Overhead |
| **Explorative Arbeit** | Beim Brainstormen koennen starre Regeln kreative Antworten einschraenken |
| **Widerspruch zum aktuellen Task** | Dauerhaftes "sei kurz" kollidiert mit "erklaere mir das ausfuehrlich" |
| **Ueberladung** | 500+ Zeilen persistenter Kontext: sinkende Befolgungsrate, hoher Token-Verbrauch |
| **Veraltete Informationen** | Kontext der nicht gepflegt wird, fuehrt zu falschen Antworten basierend auf alten Fakten |

### Die Entscheidungsregel

```
Frage dich: "Wuerde ich das einem menschlichen Assistenten
am ersten Arbeitstag erklaeren?"

JA → Persistent Context
NEIN → In-Conversation Prompt
```

---

## 6. Der Paradigmenwechsel: Von einzelnen Gespraechen zu persistenten Workspaces

### Das alte Modell: "Groundhog Day"

Jede AI-Konversation startet bei Null. Der Nutzer muss jedes Mal:
- Erklaeren wer er ist
- Den Kontext beschreiben
- Die gewuenschte Tonalitaet definieren
- Qualitaetsstandards formulieren
- Formatwuensche aeussern

Das ist wie jeden Morgen einem neuen Praktikanten alles von vorne zu erklaeren.

### Das neue Modell: "Persistent Workspace"

> "Explain your job once, not every morning."

Der Arbeitskontext ist persistent. Das System kennt:
- Deine Rolle und deinen Fachbereich
- Deinen bevorzugten Arbeitsstil
- Wiederkehrende Aufgaben und deren Standards
- Vergangene Entscheidungen und deren Begruendungen
- Was in vorherigen Sessions funktioniert hat (und was nicht)

### Drei Stufen der Persistenz

| Stufe | Beschreibung | Beispiel | Aufwand |
|-------|-------------|---------|---------|
| **1: Custom Instructions** | Statische Praeferenzen in den Einstellungen | "Ich bin PM, antworte auf Deutsch, kurze Saetze" | 10 Min einmalig |
| **2: Projekt-Kontext** | Projektspezifische Regeln und Wissen | CLAUDE.md mit Architektur, Standards, Workflows | 30 Min + Pflege |
| **3: Lernende Systeme** | System akkumuliert Wissen ueber Zeit | Auto Memory, angepasste Praeferenzen aus Korrekturen | Automatisch |

### Was sich aendert fuer Knowledge Worker

**Vorher (Transaktional):**
- Jede Anfrage ist isoliert
- Qualitaet schwankt stark
- Wiederholung bei jedem Gespraech
- "AI als Werkzeug" — man benutzt es und legt es weg

**Nachher (Relational):**
- Kontext baut sich auf
- Konsistente Qualitaet ueber Zeit
- Das System lernt Praeferenzen
- "AI als Arbeitspartner" — ein geteilter Workspace

### Praktischer Einstieg: Die 15-Minuten-Methode

1. **5 Min:** Schreibe 3 Saetze zu deiner Rolle und deinem Arbeitskontext
2. **5 Min:** Definiere 3-5 Output-Praeferenzen (Format, Laenge, Sprache, Stil)
3. **5 Min:** Formuliere 2-3 Qualitaetsregeln (wann nachfragen, was vermeiden)

Das ist dein Minimum Viable System Prompt. Verfeinere ihn ueber die naechsten Wochen basierend auf Erfahrung.

### Die Compound-Effect-These

Persistenter Kontext wird wertvoller je laenger du ihn nutzt — aber nur wenn er gepflegt wird:

```
Woche 1:  Grundregeln stehen, 60% Trefferquote
Woche 2:  Erste Korrekturen eingearbeitet, 75%
Woche 4:  Edge Cases abgedeckt, 85%
Woche 8:  Fein-Tuning, 90%+
Danach:   Nur noch Pflege bei Aenderungen
```

Der groesste Fehler: Alles auf einmal perfekt machen wollen. Der zweitgroesste: Nie anfangen.

---

## Quellen

1. **Anthropic — Prompting Best Practices** (2026): Offizielle Dokumentation zu System Prompts, XML-Strukturierung, Rollen, Beispielen, und Output-Kontrolle. https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices

2. **Claude Code — Memory Documentation** (2026): CLAUDE.md-Dateien, Auto Memory, persistenter Kontext, modulare Rules, und Workspace-Persistenz. https://code.claude.com/docs/en/memory

3. **Anthropic — Prompt Engineering Overview** (2026): Meta-Guide zu Prompt Engineering mit Verweis auf Evaluationen und Success Criteria. https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/overview

4. **OpenAI — Prompt Engineering Guide** (2024-2025): Best Practices fuer System Messages, Custom Instructions, und strukturiertes Prompting. https://platform.openai.com/docs/guides/prompt-engineering (Zugriff via Docs, nicht direkt abrufbar)

5. **Anthropic — Claude Code Best Practices** (2026): Agentic Workflows, State Management, Context Windows, und Multi-Session-Arbeit. https://www.anthropic.com/engineering/claude-code-best-practices

---

## Zusammenfassung fuer L3 Modul

**Kernbotschaften fuer Lernende:**

1. **System Prompts sind Stellenbeschreibungen** — Behandle sie wie das Onboarding eines neuen Mitarbeiters: Rolle, Kontext, Standards, Beispiele.

2. **Struktur schlaegt Laenge** — Ein kurzer, gut strukturierter Prompt (Rolle + 5 Regeln + 1 Beispiel) schlaegt einen 500-Zeilen-Roman.

3. **Positiv formulieren** — Sage was das Modell TUN soll, nicht was es lassen soll.

4. **Kontext erklaeren** — Das WARUM hinter einer Regel hilft dem Modell, sie richtig anzuwenden und zu generalisieren.

5. **Persistent Context ist ein Paradigmenwechsel** — Von "jedes Gespraech bei Null" zu "erklaer deinen Job einmal".

6. **Iterativ verfeinern** — Der beste Prompt entsteht durch Beobachten, Korrigieren, und Bereinigen ueber Wochen.

7. **Wissen wann es nicht hilft** — Einfache One-Off Fragen, schnell wechselnde Anforderungen, und explorative Arbeit brauchen keinen persistenten Kontext.
