# L3 Research: Claude Projects

Working document for the AI Fluency L3 learning module. Research compiled 2026-03-14.

---

## 1. What Are Claude Projects?

Projects are persistent, self-contained workspaces inside Claude.ai (web and desktop app) that bring together a knowledge base, custom instructions, and chat history in one place. They allow users to ground Claude's responses in uploaded documents and organizational context rather than re-explaining background information in every conversation.

Key concept: Every chat within a project automatically has access to the project's knowledge base and instructions, but **context is not shared across individual chats** within a project unless the information is added to the project knowledge base.

- Source: [What are projects? | Claude Help Center](https://support.claude.com/en/articles/9517075-what-are-projects)
- Source: [Collaborate with Claude on Projects | Anthropic Blog](https://www.anthropic.com/news/projects)

---

## 2. Availability by Plan

| Plan | Projects allowed | Knowledge base | RAG (scaling beyond context window) | Sharing |
|------|-----------------|----------------|--------------------------------------|---------|
| **Free** | Up to 5 projects | Basic uploads | No | No |
| **Pro** | Unlimited | Full uploads | Yes (automatic) | No |
| **Max** | Unlimited | Full uploads | Yes (automatic) | No |
| **Team** | Unlimited | Full uploads | Yes (automatic) | Yes (team sharing) |
| **Enterprise** | Unlimited | Full uploads | Yes (automatic) | Yes (org-wide sharing) |

Free users can create and use projects with basic knowledge uploads. Paid plans (Pro, Max, Team, Enterprise) unlock enhanced project knowledge with RAG, which automatically scales to handle large amounts of content.

- Source: [What are projects? | Claude Help Center](https://support.claude.com/en/articles/9517075-what-are-projects)

---

## 3. Knowledge Base (File Uploads)

### Supported File Types

| Category | Formats |
|----------|---------|
| **Documents** | PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON |
| **Spreadsheets** | XLSX (requires code execution enabled in account settings) |
| **Images** | JPEG, PNG, GIF, WebP |

### Upload Limits

| Parameter | Chat uploads | Project knowledge |
|-----------|-------------|-------------------|
| **File size** | 30 MB per file | 30 MB per file |
| **Number of files** | Up to 20 per chat | Unlimited (but total must fit context window; RAG expands this on paid plans) |
| **Image dimensions** | Up to 8000 x 8000 px | Up to 8000 x 8000 px |

### PDF Processing Details

- PDFs under 100 pages: Claude analyzes both text AND visual elements (images, charts, graphics)
- PDFs over 1,000 pages: Claude processes text only
- Recommended image resolution: 1,000 x 1,000 px or larger for best results

### How Knowledge Integrates into Context

- Project knowledge files are processed and made available across all chats in that project
- On paid plans, when the project knowledge approaches the context window limit, Claude automatically enables **RAG mode**, expanding capacity by up to **10x** while maintaining response quality
- Text is extracted from documents (except multimodal PDFs where visuals are also processed)
- Token limits apply based on the length of extracted content

- Source: [Uploading files to Claude | Claude Help Center](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)
- Source: [What are projects? | Claude Help Center](https://support.claude.com/en/articles/9517075-what-are-projects)

---

## 4. Custom Instructions (Project Instructions)

### What They Do

Project instructions are persistent directives that apply to **every chat** within a project. They tell Claude how to behave, what role to adopt, what context to consider, and how to format responses for that specific workspace.

### How They Differ from Other Personalization Features

| Feature | Scope | Purpose | Example |
|---------|-------|---------|---------|
| **Profile Preferences** | All conversations, account-wide | General guidance about the user | "I'm a marketing manager at a B2B SaaS company." |
| **Project Instructions** | Single project only | Specific context and behavioral rules | "Answer from the perspective of a data analyst. Use SQL examples when relevant." |
| **Styles** | Applied per conversation or globally | Response format and tone only (no context) | Concise vs. explanatory, formal vs. casual |

These three features work **independently or in combination**. Profile preferences provide global context, project instructions add project-specific depth, and styles control the delivery format.

### Best Practices for Writing Custom Instructions

Based on Anthropic's prompting best practices and the Projects documentation:

1. **Define Claude's role clearly**: "You are a senior content strategist specializing in B2B tech marketing."
2. **Provide relevant context**: "Our company sells cloud infrastructure to mid-market enterprises. Our tone is professional but approachable."
3. **Set explicit constraints**: "Always cite sources. Never make up statistics. If unsure, say so."
4. **Specify output preferences**: "Use bullet points for summaries. Include headers for sections longer than 3 paragraphs."
5. **Reference the knowledge base**: "Use the uploaded brand guidelines as the source of truth for voice and tone."
6. **Keep instructions focused**: Instructions should be specific to the project's purpose, not general preferences (those belong in Profile Preferences).

### Example Custom Instructions

**For a Content Team Project:**
```
You are a content strategist for [Company Name].

Key context:
- Our audience is CTOs and VP Engineering at companies with 100-500 employees
- Our brand voice is authoritative but conversational (see uploaded brand guide)
- We publish on blog, LinkedIn, and email newsletter

Rules:
- Always suggest a headline and meta description for blog posts
- Use the uploaded SEO keyword list when relevant
- Flag any claims that need fact-checking
- Keep paragraphs under 4 sentences
```

**For a Research Analysis Project:**
```
You are a research analyst helping me synthesize academic papers.

Rules:
- Distinguish clearly between findings, interpretations, and your own analysis
- Always note sample sizes and methodology limitations
- Use APA citation format
- When comparing studies, create a comparison table
- Rate evidence strength: Strong / Moderate / Weak / Anecdotal
```

- Source: [Understanding Claude's Personalization Features | Claude Help Center](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- Source: [How can I create and manage projects? | Claude Help Center](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Source: [Prompting best practices | Claude Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)

---

## 5. Step-by-Step: Creating a Claude Project

### Step 1: Navigate to Projects
- Go to **claude.ai/projects**, or hover over the left sidebar and select **"Projects"**

### Step 2: Create a New Project
- Click **"+ New Project"** in the upper right corner
- Enter a **project name** and **description**
- Note: Claude cannot access the project name or description as context -- they are for your organization only

### Step 3: Set Visibility (Team/Enterprise only)
- **Private**: Only you and invited members can view or use the project
- **Organization-wide**: Everyone in your organization can access it (if enabled by admin)

### Step 4: Add Project Knowledge
- In the project view, find the knowledge base in the **right sidebar**
- Click the **"+"** button to upload documents, text files, or code snippets
- All uploaded content becomes available across every chat in the project

### Step 5: Set Custom Instructions
- Click **"Set project instructions"**
- Write your behavioral guidelines (see Section 4 for best practices)
- Click **"Save instructions"**
- These instructions apply to all chats in the project

### Step 6: Start Chatting
- Begin new chats within the project -- each one automatically receives the knowledge base and instructions as context
- Remember: individual chat history is NOT shared between chats; only knowledge base content is shared

### Managing Projects

| Action | How |
|--------|-----|
| **Star a project** | Three-dot menu on Projects page, or star icon within a project (adds to sidebar for quick access) |
| **Move existing chats into a project** | Click dropdown arrow next to chat name > "Add to project" > choose destination. Bulk move from chat history page. |
| **Archive a project** | Three-dot menu. Note: archiving resets all sharing permissions to private and wipes sharing context for security. |
| **Unarchive** | Go to archived projects tab, use three-dot menu |
| **Delete** | Three-dot menu on active projects |

- Source: [How can I create and manage projects? | Claude Help Center](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

---

## 6. Project Sharing (Team & Enterprise Plans)

### How to Share

1. Open your project
2. Click **"Share project"** next to the project name
3. Add members by name/email, or bulk-paste email lists
4. Assign permission levels

### Permission Levels

| Level | Can do | Cannot do |
|-------|--------|-----------|
| **Can use** | View project contents, knowledge, and instructions; chat within the project | Edit instructions, knowledge, or member settings |
| **Can edit** | Everything above, plus modify instructions, manage knowledge, and change member access | -- |

### Discovery
- Shared projects appear in the **"Shared with me"** tab
- Members receive **email notifications** when a project is shared with them

- Source: [How can I create and manage projects? | Claude Help Center](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

---

## 7. Limitations and Constraints

### What Projects CAN Do
- Persist knowledge across multiple conversations within a project
- Apply custom instructions automatically to every chat
- Scale beyond the context window via RAG (paid plans)
- Share workspaces with team members (Team/Enterprise)
- Upload diverse file types (documents, code, images)
- Organize work into separate, focused workspaces

### What Projects CANNOT Do
- **No cross-chat memory**: Conversations within a project do not share context with each other; only the knowledge base is shared
- **No real-time data**: Projects work with uploaded static files, not live connections to databases or APIs (though Anthropic has mentioned future integrations)
- **No version control**: There is no built-in versioning for knowledge base files or instructions
- **Project name/description not in context**: Claude does not "see" the project name or description -- only the knowledge base and instructions
- **Free plan limits**: Maximum 5 projects, no RAG scaling
- **No API access**: Projects are a claude.ai feature, not available via the API (the API has its own approaches like prompt caching)
- **File size cap**: 30 MB per file maximum
- **No native integrations yet**: As of early 2026, no native app integrations (Google Drive, Notion, etc.) are live, though Anthropic has announced plans for them

### Privacy
- Data and chats shared within Projects are **not used to train generative models** without explicit user consent

- Source: [What are projects? | Claude Help Center](https://support.claude.com/en/articles/9517075-what-are-projects)
- Source: [Collaborate with Claude on Projects | Anthropic Blog](https://www.anthropic.com/news/projects)
- Source: [Uploading files to Claude | Claude Help Center](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)

---

## 8. Project Organization: Use Case Patterns

Based on Anthropic's official examples and best practices:

| Use Case | Knowledge Base Content | Custom Instructions Focus |
|----------|----------------------|--------------------------|
| **Research & Analysis** | Academic papers, reports, datasets | Citation format, evidence evaluation, methodology awareness |
| **Content Creation** | Style guides, brand docs, audience personas, SEO keywords | Tone, format preferences, platform-specific rules |
| **Product Development** | PRDs, competitor analyses, user research, specs | Role (PM, designer, engineer), decision framework |
| **Education / Course Design** | Textbooks, curricula, learning standards | Pedagogical approach, difficulty level, assessment style |
| **Personal Finance** | Statements, investment reports, tax docs | Privacy awareness, calculation precision, no financial advice disclaimers |
| **Client Work** | Client briefs, past deliverables, brand guidelines | Client-specific terminology, deliverable formats |
| **Code Review / Engineering** | Codebase docs, architecture decisions, style guides | Language preferences, testing standards, review criteria |

### Organization Tips

1. **One project per distinct context**: Don't mix unrelated work. A "Marketing" project and a "Engineering" project should be separate.
2. **Use instructions for rules, knowledge base for facts**: Instructions tell Claude HOW to behave; knowledge base provides WHAT to reference.
3. **Update knowledge base as context evolves**: Remove outdated documents, add new ones. The knowledge base is the project's source of truth.
4. **Star frequently-used projects**: They appear in your sidebar for quick access.
5. **Archive completed projects**: Keeps your workspace clean. You can unarchive later if needed.

- Source: [Examples of projects you can create | Claude Help Center](https://support.claude.com/en/articles/9529781-examples-of-projects-you-can-create)

---

## 9. Related Features (Context for L3 Module)

### Styles
Styles control HOW Claude responds (tone, length, format) and can be combined with project instructions. They are a separate feature from Projects but complement them. Users can create custom styles based on their own writing samples.

- Source: [Configure and use styles | Claude Help Center](https://support.claude.com/en/articles/10181068-configure-and-use-styles)

### Skills
Skills are a newer feature (2026) where Claude can load specialized instruction sets for specific tasks. Skills are folders with instructions, scripts, and resources. They differ from Projects in that Skills are task-oriented templates, while Projects are workspace-oriented containers.

- Source: [What are Skills? | Claude Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)

---

## Sources Index

All sources used in this research document:

1. [Collaborate with Claude on Projects | Anthropic Blog](https://www.anthropic.com/news/projects)
2. [What are projects? | Claude Help Center](https://support.claude.com/en/articles/9517075-what-are-projects)
3. [How can I create and manage projects? | Claude Help Center](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
4. [Examples of projects you can create | Claude Help Center](https://support.claude.com/en/articles/9529781-examples-of-projects-you-can-create)
5. [Understanding Claude's Personalization Features | Claude Help Center](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
6. [Uploading files to Claude | Claude Help Center](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)
7. [Prompting best practices | Claude Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
8. [Configure and use styles | Claude Help Center](https://support.claude.com/en/articles/10181068-configure-and-use-styles)
9. [What are Skills? | Claude Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)

---

## 10. Custom GPTs (OpenAI)

### Was sind Custom GPTs?

Custom GPTs sind spezialisierte ChatGPT-Versionen, die Nutzer ueber den GPT Builder erstellen koennen. Jeder Custom GPT kombiniert drei Elemente: Instructions (System Prompt), Knowledge Files (hochgeladene Dokumente) und optionale Actions (API-Aufrufe). Sie sind seit November 2023 verfuegbar und koennen ueber den GPT Store geteilt werden.

### Erstellung

1. **GPT Builder oeffnen**: Ueber "Create a GPT" im ChatGPT-Interface (Plus/Team/Enterprise)
2. **Instructions schreiben**: Freitext-Feld fuer den System Prompt — Rolle, Regeln, Verhalten
3. **Knowledge Files hochladen**: PDFs, DOCX, TXT, CSV, etc. — werden fuer RAG indiziert
4. **Actions konfigurieren** (optional): OpenAPI-Specs fuer externe API-Aufrufe
5. **Veroeffentlichen**: Privat, per Link, oder im GPT Store

### Knowledge Files

- Hochgeladene Dateien werden als Retrieval-Kontext verwendet (RAG)
- Maximale Dateien: 20 Dateien, je bis zu 512 MB (aber praktisch durch Token-Limits begrenzt)
- Unterstuetzte Formate: PDF, DOCX, PPTX, TXT, CSV, JSON, und weitere
- Die Dateien werden automatisch indiziert — der GPT durchsucht sie bei relevanten Fragen
- WICHTIG: Knowledge Files sind NICHT sicher. Nutzer koennen mit gezielten Prompts den Inhalt extrahieren

### Instructions (System Prompt)

- Freitext bis ca. 8.000 Zeichen
- Werden bei JEDER Konversation als System Prompt geladen
- Best Practices: Rolle definieren, Antwortformat festlegen, Grenzen setzen
- Aehnlich wie Claude Projects Custom Instructions, aber ohne separate UI fuer Knowledge vs. Instructions

### Vergleich: Custom GPTs vs. Claude Projects

| Merkmal | Custom GPTs | Claude Projects |
|---------|------------|-----------------|
| **Ersteller** | Jeder Plus/Team/Enterprise-Nutzer | Jeder Claude-Nutzer (Free: 5 Projekte) |
| **Teilbarkeit** | GPT Store, Link, oder privat | Team/Enterprise: Team-Sharing |
| **Knowledge Base** | Files hochladen (RAG) | Files hochladen (RAG auf Paid) |
| **Instructions** | Ein Freitext-Feld | Separates Instructions-Feld |
| **Actions** | Ja (API-Aufrufe via OpenAPI) | Nein (kein API-Zugriff) |
| **Monetarisierung** | GPT Store (Programm eingestellt 2025) | Nein |
| **Sicherheit Knowledge** | Extrahierbar durch Nutzer | Im Projekt-Kontext geschuetzt |
| **Code Execution** | Ja (Code Interpreter) | Ja (Analysis Tool) |
| **Multi-Chat-Kontext** | Nein (jeder Chat startet neu) | Knowledge Base gilt fuer alle Chats |

### Limitierungen

- Knowledge Files koennen durch Prompt Injection extrahiert werden
- Kein echtes "Memory" ueber Sessions — jede Konversation startet bei Null
- GPT Store Monetarisierung wurde Mitte 2025 eingestellt
- Actions erfordern technische Kenntnisse (OpenAPI-Specs)
- Keine native Team-Kollaboration an einem GPT (nur Sharing)

### Staerken

- Einfacher, visueller Builder (kein Code noetig)
- GPT Store als Discovery-Plattform (>3 Mio. GPTs, Stand 2025)
- Actions ermoeglichen echte Tool-Integration
- Breiteste Nutzerbasis aller AI-Plattformen

- Quellen: OpenAI Help Center (Custom GPTs), OpenAI Blog (Introducing GPTs, Nov 2023), GPT Store Launch (Jan 2024)

---

## 11. Microsoft 365 Copilot

### Was ist M365 Copilot?

Microsoft 365 Copilot ist ein AI-Assistent, der direkt in die Microsoft 365 Apps integriert ist (Word, Excel, PowerPoint, Outlook, Teams, OneNote, etc.). Anders als Claude Projects oder Custom GPTs arbeitet Copilot nicht in einer eigenen Chat-Oberflaeche, sondern innerhalb der bestehenden Arbeitstools. Das Kernprinzip: Die AI hat Zugriff auf die organisationalen Daten des Nutzers — E-Mails, Dokumente, Kalender, Chats — ueber den Microsoft Graph.

### Kontext-Architektur

M365 Copilot nutzt ein dreistufiges Kontext-Modell:

1. **Microsoft Graph Grounding**: Zugriff auf E-Mails, Dateien, Kalender, Teams-Chats, SharePoint-Dokumente. Der "Kontext" ist nicht hochgeladen, sondern LIVE aus dem Arbeitsalltag.
2. **Web Grounding**: Optionaler Zugriff auf aktuelle Web-Informationen fuer Faktenpruefung und Ergaenzung
3. **User Prompt**: Die konkrete Anweisung des Nutzers

### Copilot pro App

| App | Typische Funktionen | Kontext-Quelle |
|-----|---------------------|----------------|
| **Word** | Entwuerfe generieren, umschreiben, zusammenfassen | Aktuelles Dokument + referenzierte Dateien |
| **Excel** | Formeln vorschlagen, Daten analysieren, Visualisierungen | Aktuelle Tabelle |
| **PowerPoint** | Praesentationen aus Dokumenten erstellen, Design | Referenzierte Word/PDF-Dateien |
| **Outlook** | E-Mails zusammenfassen, antworten, Threads analysieren | E-Mail-Verlauf, Kalender |
| **Teams** | Meeting-Zusammenfassungen, Chat-Zusammenfassungen, Action Items | Meeting-Transkripte, Chat-Verlaeufe |
| **OneNote** | Notizen zusammenfassen, To-Dos extrahieren | Aktuelle Notizbuecher |

### Preismodell (Stand Anfang 2026)

| Plan | Preis | Zielgruppe |
|------|-------|-----------|
| **Copilot Pro** (Einzelnutzer) | ~20 USD/Monat | Einzelpersonen mit M365 Personal/Family |
| **Copilot for Microsoft 365** (Business) | ~30 USD/Nutzer/Monat | Unternehmen mit M365 Business/Enterprise |

### Vergleich: M365 Copilot vs. Claude Projects vs. Custom GPTs

| Merkmal | M365 Copilot | Claude Projects | Custom GPTs |
|---------|-------------|-----------------|------------|
| **Kontext-Quelle** | Live-Daten (Graph) | Hochgeladene Dateien | Hochgeladene Dateien |
| **Integration** | In M365 Apps eingebettet | Eigene Web-Oberflaeche | ChatGPT-Interface |
| **Setup** | Admin-Deployment | Nutzer erstellt Projekt | Nutzer erstellt GPT |
| **Wer kontrolliert Kontext** | Organisation + Nutzer | Nutzer | Nutzer |
| **Datensicherheit** | Enterprise-Grade, Compliance | Daten nicht fuer Training | Extrahierbar |
| **Staerke** | Nahtlose Workflow-Integration | Flexibler Projekt-Workspace | Teilbar, Actions |
| **Schwaeche** | Nur in M365, teuer | Nur in Claude.ai | Knowledge unsicher |

### Limitierungen

- **Preis**: 30 USD/Nutzer/Monat fuer Business — signifikante Investition
- **Lock-in**: Nur sinnvoll innerhalb des Microsoft-Oekosystems
- **Qualitaet variiert**: In manchen Apps (Excel) noch eingeschraenkt
- **Admin-Abhaengigkeit**: IT-Admin muss Copilot freigeben und konfigurieren
- **Datenschutz**: Nutzer muessen verstehen, auf welche Daten Copilot zugreift
- **Kein Custom Training**: Keine Moeglichkeit, das Modell auf eigene Daten zu trainieren

### Was M365 Copilot fuer L3 bedeutet

M365 Copilot zeigt einen fundamental anderen Ansatz als Claude Projects oder Custom GPTs:
- Kontext wird NICHT hochgeladen, sondern ist LIVE aus dem Arbeitsalltag
- Der Nutzer konfiguriert keinen System Prompt — die Integration IST der Kontext
- Das Konzept verschiebt sich von "AI als Werkzeug" zu "AI eingebettet in bestehende Workflows"

- Quellen: Microsoft Learn (M365 Copilot Overview, Copilot Architecture), Microsoft 365 Pricing Pages, Microsoft Copilot Blog
