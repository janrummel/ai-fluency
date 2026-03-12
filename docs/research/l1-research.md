# L1 Research: First Steps with AI
**Working document — not for publication**
**Research date: 2026-03-12**
**Purpose: Factual basis for L1 "First Steps with AI" learning module (DE+EN)**

---

## 1. Current AI Chatbot Landscape (March 2026)

### 1.1 ChatGPT (OpenAI)

**Current Models (as of March 2026):**
- GPT-5.4 Pro / GPT-5.4 Thinking / GPT-5.3 Instant — latest generation
- o3, o4-mini, o4-mini-high — reasoning models
- GPT-4o — still available for Free tier users (with usage limits)
- GPT-4.1 — optimized for code
- Note: GPT-5.1 models retired as of March 11, 2026; conversations auto-migrated to GPT-5.3/5.4

**Pricing Tiers [March 2026 — pricing may change]:**

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | GPT-4o (limited), web search, basic features |
| Go | $8/month | GPT-5.2 Instant, file/image support, more messages |
| Plus | $20/month | GPT-4o, o3, o4-mini, GPT-4.1, GPT-4.5 preview |
| Pro | $200/month | Unlimited access to all models including o1, o3-pro, GPT-5.2, advanced voice |
| Team | $25-30/user/month | Unlimited GPT-4o + 4.1-mini, generous advanced model limits |
| Enterprise | Custom | Everything in Team + expanded context, security features |

**Key Features:**
- Web search (available in Free tier)
- Image generation (DALL-E integration)
- Code interpreter / Advanced Data Analysis
- Voice mode (advanced in Pro)
- Memory across conversations (paid plans)
- Custom GPTs
- Canvas (collaborative writing/coding workspace)

---

### 1.2 Claude (Anthropic)

**Current Models (as of March 2026):**
- Claude Opus 4.6 — most intelligent, released February 5, 2026
- Claude Sonnet 4.6 — high capability, balanced speed/intelligence
- Claude Opus 4.5 — previous top tier
- Claude Sonnet 4.5 — available on Free tier
- Claude Haiku 4.5 — fast, lightweight, available on Free tier

**Pricing Tiers [March 2026 — pricing may change]:**

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Sonnet 4.5 + Haiku 4.5, 30-100 messages/day, no Opus, no Cowork |
| Pro | $20/month | All models incl. Opus 4.6, Cowork, Claude Code, Research tool |
| Max | $100/month | 5x Pro limits, 1M context window, agent teams (preview) |
| Max 20x | $200/month | 20x Pro limits, highest priority |
| Team | $25-125/seat | Business features, data not used for training |
| Enterprise | Custom | Full admin controls, SSO, audit logs |

**Key Features:**
- Cowork: Agentic tool where Claude can read/modify files in designated folders, make plans, execute multi-step tasks — "Claude Code for non-developers." Available on Pro+. Now on Windows + macOS. Connectors for Google Drive, Gmail, DocuSign, etc.
- Artifacts (interactive outputs in conversation)
- Projects (organized workspaces with custom instructions)
- Research tool (deep web research)
- Claude Code (CLI for developers)
- 200K token context window standard (1M on Max)

**Cowork Detail (for L1 content):**
Cowork is Anthropic's agentic feature that lets Claude complete work with much more agency than a regular chat. You designate folders Claude can access, give instructions through chat, and Claude makes a plan and works through it — asking permission before significant actions. Think of it as a capable assistant that can actually do the work on your computer, not just talk about it. Microsoft also launched "Copilot Cowork" integrating Claude into M365 (March 2026).

---

### 1.3 Google Gemini

**Current Models (as of March 2026):**
- Gemini 3.1 Pro — latest, advanced reasoning (released Feb 19, 2026)
- Gemini 3 Flash — default model in Gemini app, fast + capable
- Gemini 3.1 Flash Lite — released March 3, 2026
- Gemini 2.5 Flash — still available, good balance of speed/intelligence
- Gemini 2.5 Flash-Lite — budget option
- Note: Gemini 3 Pro Preview deprecated March 9, 2026; Gemini 2.0 models retiring June 1, 2026

**Pricing Tiers [March 2026 — pricing may change]:**

| Plan | Price | Key Features |
|------|-------|-------------|
| Free | $0 | Gemini 2.5 Flash, limited 2.5 Pro, Deep Research, Gemini Live, Canvas, Gems |
| Google AI Pro | $19.99/month | Gemini 3 access, Deep Research, 2TB storage, AI in Gmail/Docs/etc. |
| Google AI Ultra | ~$42/month ($124.99/3 months) | Gemini 3 Pro, Veo 3.1 video, Deep Think, everything in Pro |

**Key Features:**
- Deep integration with Google Workspace (Gmail, Docs, Sheets, Slides, Drive)
- Gemini Live (conversational voice mode)
- Deep Research (autonomous research agent)
- Canvas (collaborative workspace)
- Gems (custom AI personas)
- Veo 3.1 video generation (Ultra tier)
- NotebookLM (separate tool, but part of Google AI ecosystem)
- Multimodal: text, image, audio, video understanding

**Key Differentiator:** Best for users already in the Google ecosystem. AI Pro subscription integrates directly into Gmail, Docs, Sheets — no separate tool needed.

---

### 1.4 Microsoft Copilot

**Current State (March 2026):**
Copilot exists in two main forms:
1. **Copilot (standalone)** — Free chatbot at copilot.microsoft.com / in Bing/Edge
2. **Microsoft 365 Copilot** — Paid add-on integrated into Word, Excel, PowerPoint, Outlook, Teams

**Pricing [March 2026 — pricing changes coming July 2026]:**

| Plan | Price | Key Features |
|------|-------|-------------|
| Free (Copilot) | $0 | GPT-5.2 chat, web answers, Think Deeper, limited image creation, file upload (20 files/50MB each) |
| Copilot Business | $18-21/user/month | M365 app integration, org data access |
| M365 Copilot (Enterprise) | $30/user/month ($23/user/year promo through March 2026) | Full M365 integration, agents, security |
| M365 E7 (new, May 2026) | $99/user/month | Copilot + Entra identity + Agent 365 bundle |

**What Free Copilot Can Do:**
- Chat with GPT models (GPT-5.2 available)
- Web-grounded answers
- Creative writing, summarization
- Think Deeper (reasoning mode, may be slower during peak hours)
- Voice mode
- Image generation (limited "boosts")
- File upload (PDF, DOCX, XLSX, PPTX, CSV, JSON)

**What Free Copilot Cannot Do:**
- No integration with your M365 apps (Word, Excel, etc.)
- No access to organizational/company data
- No real-time collaboration in documents
- Lower priority during peak hours
- No agents or workflow automation

**What Paid M365 Copilot Adds:**
- Copilot embedded in Word, Excel, PowerPoint, Outlook, Teams
- Access to organizational data (emails, files, meetings)
- Real-time meeting summaries in Teams
- Document drafting/editing in context
- Copilot Pages (shared AI workspace)
- AI agents for workflow automation

**Key Differentiator:** Only option deeply integrated into Microsoft 365. If your company lives in M365, this is the most natural AI integration — but it requires a paid license for the real value.

**Note:** Microsoft also announced "Copilot Cowork" powered by Anthropic's Claude, integrating into M365 (March 2026). This signals a multi-model approach.

---

### 1.5 Comparison Summary

**What's Free (March 2026):**

| Tool | Free Model | Messages/Day | Key Limitation |
|------|-----------|-------------|----------------|
| ChatGPT | GPT-4o (limited) | Limited | No advanced reasoning models, usage caps |
| Claude | Sonnet 4.5 + Haiku 4.5 | 30-100 | No Opus, no Cowork, peak-hour restrictions |
| Gemini | 2.5 Flash + limited 2.5 Pro | Not published | Limited Pro access, no Workspace integration |
| Copilot | GPT-5.2 | Not published | No M365 integration, lower priority at peak |

**Key Differentiators:**

| Tool | Best For | Unique Strength |
|------|---------|----------------|
| ChatGPT | Most versatile, largest ecosystem | Custom GPTs, broadest model selection, most plugins |
| Claude | Careful reasoning, long documents, coding | Largest context window (200K-1M), Cowork agentic feature, safety focus |
| Gemini | Google ecosystem users | Native Gmail/Docs/Sheets integration, Deep Research, multimodal |
| Copilot | Microsoft 365 organizations | Only AI embedded in Word/Excel/PowerPoint/Outlook/Teams |

**Price Comparison (individual paid, lowest tier):**
- ChatGPT Plus: $20/month
- Claude Pro: $20/month
- Google AI Pro: $19.99/month
- Copilot Business: $18-21/user/month

---

## 2. Common Beginner Misconceptions

### 2.1 "AI knows everything" / "AI is always right"

**Reality:** AI models are trained on a snapshot of internet text up to a cutoff date. They do not have access to all information, and the information they have may be outdated or biased by training data composition.

**Key point for learners:** What we are building is "artificial memory" — AI remembers vast amounts of what has been written, but it does not understand *why* it was written, for whom, or with what consequences. It can recall patterns but cannot verify truth.

**Practical implication:** AI can confidently state incorrect facts. Unlike a search engine that points you to sources, a chatbot presents information as authoritative text — making errors harder to spot.

### 2.2 "AI understands me" (vs. pattern matching)

**Reality:** Contemporary AI systems do not understand language in any cognitive or semantic sense. They operate by identifying statistical patterns across massive datasets. Models like GPT-5, Claude, and Gemini do not contain mental representations or grounded concepts.

**Good analogy for learners:** AI is like a very sophisticated autocomplete system. When you type a message, it predicts the most likely next words based on patterns it learned from billions of text examples. It doesn't "know" what a tree is — it knows that the word "tree" tends to appear near words like "leaf," "branch," "forest."

**The debate (for advanced learners):** Geoffrey Hinton argues that "to predict the next word accurately, you have to understand the sentence." Whether this constitutes "understanding" in a meaningful sense is actively debated. For beginners, the safe message is: treat AI outputs as suggestions to verify, not as understood answers.

### 2.3 "AI remembers everything I told it" (context window limits)

**Reality:** Each AI conversation has a "context window" — a limited amount of text the model can "see" at once. Think of it as the AI's short-term memory or working desk.

**Key facts:**
- Context windows range from ~128K tokens (ChatGPT) to 200K-1M tokens (Claude Max)
- Roughly: 100K tokens is about 75,000 words or ~300 pages of text
- Beyond the window, earlier parts of conversation are dropped
- Even within the window, AI handles beginning and end better than the middle ("lost in the middle" problem)
- Bigger context windows do not mean the model "knows" more — just that it can work with more information in the moment

**Memory features (paid plans):** ChatGPT and Claude offer "memory" features that persist across conversations, but these store summaries/key facts, not full conversations. They are opt-in and imperfect.

**Practical implication:** In long conversations, AI may "forget" what you said earlier. Starting fresh conversations for new topics is often better than one endless thread.

### 2.4 "AI is dangerous / will take my job"

**Reality (based on research as of early 2026):**

**Job impact — what the data shows:**
- After ChatGPT's launch, job postings for structured/repetitive tasks decreased ~13%, while demand for analytical/technical/creative work grew ~20%
- WEF projects 170 million new jobs by 2030, with 92 million displaced — net gain of 78 million positions
- PwC research shows job numbers are rising in virtually every type of AI-exposed occupation
- AI may substitute for entry-level routine work but augment experienced workers

**The balanced message for beginners:**
- AI is reshaping *how* work is performed, not eliminating work wholesale
- Skills evolution and continuous learning are becoming essential
- "AI won't take your job — but someone who knows how to use AI might"
- The threat is less "replacement" and more "skills gap" for those who don't adapt

**The danger framing:**
- Legitimate concerns exist (misinformation, bias amplification, privacy, deepfakes)
- But apocalyptic framing ("AI will destroy humanity") is not supported by current evidence
- The productive approach: understand capabilities and limitations, use responsibly

### 2.5 Data Privacy — What Actually Happens with Your Data

**The core message: Your conversations are not necessarily private. Policies differ significantly.**

**ChatGPT (OpenAI) [as of March 2026]:**
- Default: Conversations ARE used to train models
- Opt-out: Go to Settings > Data Controls > "Improve the model" → OFF
- Even when opted out: Data retained for 30 days for safety/abuse monitoring
- Team/Enterprise: Contractual guarantee — data NOT used for training
- Note: Human reviewers may read conversations for safety review

**Claude (Anthropic) [as of March 2026]:**
- IMPORTANT POLICY CHANGE (September 2025): Anthropic shifted from "no training" to opt-out model
- Default for consumer plans: Data CAN be used for training (if user doesn't opt out)
- Opt-out: Settings > Privacy > "Help improve Claude" → OFF
- If opted in: Data retained for 5 years
- If opted out: Data retained for 30 days
- If you delete a chat: It will not be used for training
- Team/Enterprise/API: Data NOT used for training (contractual guarantee)
- Previous reputation as "privacy-first" no longer fully accurate for free/consumer plans

**Gemini (Google) [as of March 2026]:**
- Default: Conversations saved for 18 months, used to improve models
- Adjustable: Can set auto-delete to 3, 18, or 36 months, or turn off entirely
- Human reviewers may examine conversations
- Setting: "Gemini Apps Activity" — control in Google account
- Google Cloud / Vertex AI: Contractual guarantee — data NOT used for training

**Microsoft Copilot [as of March 2026]:**
- Free Copilot: Standard Microsoft privacy terms apply
- M365 Copilot (Business/Enterprise): Data stays within your Microsoft 365 tenant, not used for training

**Key Privacy Rules for Beginners (5 rules):**
1. **Never share passwords, financial details, or personal health info** with any AI chatbot
2. **Check your privacy settings** on first use — opt out of training if you want privacy
3. **Assume someone might read it** — all providers retain data for at least 30 days
4. **Paid/business plans are more private** — contractual data protection
5. **Delete conversations** you don't want stored — most platforms allow this

---

## 3. AI Hallucinations

### 3.1 What Are Hallucinations?

**Definition:** AI hallucinations are outputs that are factually incorrect, fabricated, or nonsensical — but presented with the same confidence as correct information. The AI does not "know" it is wrong.

**Why the term "hallucination":** Like a human hallucination, the AI perceives (generates) something that isn't real. Some researchers prefer "confabulation" (from psychology — confidently filling in memory gaps with fabricated details).

### 3.2 Why Do Hallucinations Happen?

**Technical explanation (simplified for L1):**
1. AI generates text by predicting the most likely next word/token based on patterns
2. It has no internal model of "truth" — only statistical associations between words
3. When it encounters a gap (e.g., asked about something not well-covered in training data), it fills the gap with plausible-sounding text
4. It optimizes for "sounding right" not "being right"
5. If fabricating a detail makes the answer look more complete or convincing, the model will do it

**Good analogy for learners:** Imagine a student who has read thousands of textbooks but never attended a single class or lab. When asked a question on the exam, they write a confident, well-structured answer that *sounds* exactly like a textbook — but may contain invented facts, because they're reconstructing from patterns, not from understanding.

### 3.3 Famous Examples

**Mata v. Avianca (2023) — The case that started it all:**
- Lawyer Steven Schwartz used ChatGPT for legal research
- ChatGPT generated six completely fabricated court cases with realistic-sounding names, citations, and even case numbers
- The lawyer submitted them to court without verification
- Judge imposed sanctions; case became international news

**Scale of the problem (as of late 2025):**
- A hallucination database tracks 486+ cases in US courts alone
- Researchers identified an estimated 712+ legal decisions worldwide involving hallucinated content
- ~90% of these occurred in 2025, suggesting the problem is growing as AI adoption increases (not because AI got worse, but because more people use it without verification)

**MyPillow CEO case (2025):**
- Two attorneys fined $3,000 each for a filing with 24+ AI-generated errors including hallucinated cases

**Noland v. Land of the Free (2025):**
- $10,000 sanction for two appellate briefs containing fake citations

**New wrinkle (September 2025):**
- Lawyers now being sanctioned for failing to detect *opposing counsel's* hallucinated citations — raising the bar for everyone

### 3.4 How to Verify AI Output

**Three-step verification for beginners:**

1. **Cross-check facts:** Search for specific claims, names, dates, statistics independently. If the AI cites a study, find that study.
2. **Ask for sources:** Request the AI to provide sources — then verify those sources exist and actually say what the AI claims.
3. **Use the "too perfect" test:** If an answer seems suspiciously complete and perfectly structured, be extra skeptical. Real information often has nuance, caveats, and messy edges.

**Red flags for hallucinations:**
- Very specific numbers or statistics without a clear source
- Citations to papers, cases, or studies you can't find online
- Confident answers about very recent events (may not be in training data)
- Biographical details about non-famous people
- Detailed technical specifications that seem "too perfect"

---

## 4. Beginner-Friendly Explanation of Generative AI

### 4.1 Good Analogies

**Autocomplete on steroids:**
"You know how your phone suggests the next word when you type a message? AI works on the same principle, but at a massive scale. Instead of predicting the next word from your texts, it predicts from billions of documents — books, websites, code, conversations. It's autocomplete that can write entire essays."

**Jazz improvisation:**
"A jazz musician has internalized thousands of songs, chord progressions, and musical patterns. When they improvise, they don't play from memory — they create something new that *sounds right* based on everything they've absorbed. AI does the same with text: it creates new text that follows the patterns it learned, without copying any specific source."

**The world's best study group partner (who sometimes makes stuff up):**
"Imagine a study partner who has read every textbook, every Wikipedia article, every forum post on every topic. They can explain things clearly, summarize, and help you brainstorm. But they have a quirk: when they don't know something, they make something up — confidently — instead of saying 'I don't know.' That's AI."

**A mirror, not a brain:**
"AI reflects patterns from human knowledge back at you. It doesn't have its own thoughts, opinions, or understanding. It's a very sophisticated mirror that shows you what human-written text on your topic typically looks like."

### 4.2 What Are Tokens? (Simple Explanation)

**The simple version:**
Tokens are the "pieces" AI uses to read and write text. A token is usually a word or part of a word.

**Examples:**
- "apple" = 1 token
- "friendship" = 2 tokens ("friend" + "ship")
- "I love pizza" = 3 tokens
- A typical page of text = ~300 tokens
- A full novel = ~100,000 tokens

**Why it matters for users:**
- AI has a "token budget" — it can only process so many tokens at once (its context window)
- Pricing (for API/developer use) is based on tokens processed
- Knowing this helps explain why long conversations eventually "lose" earlier context

### 4.3 Why AI Gives Different Answers Each Time (Temperature)

**The simple version:**
AI doesn't have one fixed answer for each question. It calculates probabilities for thousands of possible next words and picks one. A setting called "temperature" controls how adventurous those picks are.

**Low temperature (0.0-0.3):** AI plays it safe — picks the most likely words. Answers are consistent, focused, predictable. Good for: factual questions, code, math.

**High temperature (0.7-1.0):** AI takes more risks — sometimes picks less likely but more creative words. Answers are varied, surprising, occasionally weird. Good for: brainstorming, creative writing, exploring ideas.

**Analogy:** Temperature is like the dial between "follow the recipe exactly" and "improvise in the kitchen." Both approaches have their place.

**Why this matters for beginners:** This is why you can ask the same question twice and get different (but usually similar) answers. It's not a bug — it's a feature. The variability also means you can regenerate an answer if you don't like the first one.

### 4.4 What Is Training Data? (Simple Explanation)

**The simple version:**
Before an AI can chat with you, it needs to "study." Its study material is called training data — a massive collection of text from the internet, books, academic papers, code repositories, and more.

**Key points:**
- Training happens *before* you use the AI — it's like school before the job
- The AI doesn't "remember" specific sources — it learns patterns and associations
- Training data has a cutoff date — the AI doesn't automatically know about events after that date
- The quality and diversity of training data directly affects the AI's capabilities and biases
- Training data may contain errors, biases, and outdated information — which the AI can reproduce

**What training data is NOT:**
- It's not a database the AI searches through (like Google)
- It's not stored conversations from other users (for reputable providers)
- It's not a perfect representation of all human knowledge

**Analogy:** Training data is like the books a student reads before graduation. After graduation (training), the student answers questions from memory and learned patterns — not by looking things up in those books. The student's knowledge is only as good as the books they read.

---

## 5. Data Privacy Policies (Detailed)

### 5.1 ChatGPT / OpenAI

**Consumer plans (Free, Go, Plus, Pro):**
- Default: Conversations used for model training
- Opt-out available: Settings > Data Controls > "Improve the model" → OFF
- When opted out: Data still retained for 30 days for safety/abuse review
- Human reviewers may read flagged conversations
- Temporary chats: Not used for training, deleted after 30 days

**Business plans (Team, Enterprise):**
- Data NOT used for training (contractual)
- Enterprise: SOC 2 compliant, admin controls, SSO
- Team: Data excluded from training, workspace management

**API:**
- Data NOT used for training by default (since March 2023)
- 30-day retention for abuse monitoring (can request zero retention)

### 5.2 Claude / Anthropic

**CRITICAL POLICY CHANGE (September 2025):**
Anthropic shifted from a "no training on conversations" default to an opt-out model. This was a significant shift that changed the privacy landscape.

**Consumer plans (Free, Pro, Max):**
- Default: If user does not opt out, data may be used for training
- Opt-out: Settings > Privacy > "Help improve Claude" → OFF
- Opted in: Data retained for 5 years
- Opted out: Data retained for 30 days
- Deleted chats: Not used for training
- Conversations flagged for safety review: May still be used regardless of setting

**Business plans (Team, Enterprise):**
- Data NOT used for training (contractual guarantee under Commercial Terms)
- Same applies to API, Amazon Bedrock, Google Vertex AI access

### 5.3 Google Gemini

**Consumer (Free, AI Pro, AI Ultra):**
- Default: Conversations saved for 18 months and used to improve models
- Human reviewers may read conversations
- Adjustable: Auto-delete at 3, 18, or 36 months, or off
- Setting: Google Account > "Gemini Apps Activity"
- Note: Even with activity off, some data may be retained for safety

**Business (Google Workspace with Gemini):**
- Covered by Google Workspace data processing terms
- Not used for model training

**Developer (Vertex AI):**
- Contractual guarantee: Data NOT used for training foundation models

### 5.4 Microsoft Copilot

**Free Copilot:**
- Standard Microsoft Services Agreement
- Conversations may be used to improve services
- Microsoft's privacy dashboard offers some controls

**M365 Copilot (Business/Enterprise):**
- Data stays within Microsoft 365 tenant
- Not used for training AI models
- Compliant with existing M365 data governance
- Inherits organization's security and compliance settings

### 5.5 Summary Table: Privacy Defaults

| Provider | Free Plan Default | Opt-Out Available? | Business Plan | Retention (opted out) |
|----------|------------------|-------------------|---------------|----------------------|
| ChatGPT | Training ON | Yes | No training | 30 days |
| Claude | Training ON (since Sep 2025) | Yes | No training | 30 days |
| Gemini | Training ON, 18mo retention | Yes | No training | Varies |
| Copilot | Improvement ON | Limited | No training | Per MS policy |

---

## Research Sources

### ChatGPT Pricing & Models
- [ChatGPT Plans and Pricing](https://chatgpt.com/pricing/)
- [OpenAI Business Pricing](https://openai.com/business/chatgpt-pricing/)
- [ChatGPT Plans Compared (IntuitionLabs)](https://intuitionlabs.ai/articles/chatgpt-plans-comparison)
- [ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [Retiring GPT-4o and Other Models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)

### Claude Pricing & Models
- [Claude Plans & Pricing](https://claude.com/pricing)
- [Claude AI Pricing 2026 (screenapp.io)](https://screenapp.io/blog/claude-ai-pricing)
- [Claude Free vs Pro vs Max 2026](https://freeacademy.ai/blog/claude-free-vs-pro-vs-max-comparison-2026)

### Claude Cowork
- [Introducing Cowork (Anthropic Blog)](https://claude.com/blog/cowork-research-preview)
- [Anthropic's Cowork Tool (TechCrunch)](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)
- [Anthropic Updates Cowork (CNBC)](https://www.cnbc.com/2026/02/24/anthropic-claude-cowork-office-worker.html)

### Google Gemini
- [Gemini Models (Google AI)](https://ai.google.dev/gemini-api/docs/models)
- [Google AI Plans (Google One)](https://one.google.com/about/google-ai-plans/)
- [Gemini Pricing 2026 (screenapp.io)](https://screenapp.io/blog/gemini-pricing)
- [Google AI Pro & Ultra Features (9to5Google)](https://9to5google.com/2026/02/21/google-ai-pro-ultra-features/)

### Microsoft Copilot
- [Microsoft 365 Copilot Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/)
- [Microsoft 365 in 2026 (EASI)](https://blog.easi.net/en/microsoft-365-in-2026-new-capabilities-copilot-skus-and-pricing)
- [Copilot Free vs Licensed (Get Support)](https://www.getsupport.co.uk/blog/2025-10/microsoft-365-copilot-free-vs-licensed-versions-explained/)
- [Copilot Changes March 2026 (SimplySharePoint)](https://simplysharepoint.com/microsoft-copilot-changes-march-2026-update-free-version/)
- [Microsoft E7 Announcement (CNBC)](https://www.cnbc.com/2026/03/09/microsoft-office-365-e7-copilot-ai.html)

### AI Hallucinations
- [AI Hallucination Cases Database (Damien Charlotin)](https://www.damiencharlotin.com/hallucinations/)
- [Lawyers Falling for AI Hallucinations (Cronkite News)](https://cronkitenews.azpbs.org/2025/10/28/lawyers-ai-hallucinations-chatgpt/)
- [AI Hallucinations in Legal Filings (LawSites)](https://www.lawnext.com/2025/05/ai-hallucinations-strike-again-two-more-cases-where-lawyers-face-judicial-wrath-for-fake-citations.html)
- [MyPillow Hallucination Case (NPR)](https://www.npr.org/2025/07/10/nx-s1-5463512/ai-courts-lawyers-mypillow-fines)

### AI Misconceptions & Understanding
- [AI Knows Everything But Understands Nothing (Medium)](https://medium.com/@sergey.podgorny/ai-knows-everything-but-understands-nothing-bc5a8c8156ad)
- [Myths of AI (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2666920X2300022X)
- [Context Window Explained (Inference Brief)](https://inferencebrief.ai/concepts/context-window)

### AI & Jobs
- [AI Augmentation vs Replacement (Harvard Business School)](https://www.library.hbs.edu/working-knowledge/enhance-or-eliminate-how-ai-will-likely-change-these-jobs)
- [AI and Workers (Johns Hopkins)](https://hub.jhu.edu/2026/02/23/will-ai-make-human-workers-obsolete/)
- [AI at WEF 2026](https://www.newkerala.com/news/a/wef-2026-ai-wont-replace-human-jobs-augment-928.htm)
- [MIT Sloan AI Research](https://mitsloan.mit.edu/press/new-mit-sloan-research-suggests-ai-more-likely-to-complement-not-replace-human-workers)

### Data Privacy
- [AI Chatbot Data Privacy Comparison (Medium)](https://medium.com/@aftab001x/the-truth-about-ai-chatbot-data-privacy-what-chatgpt-gemini-and-claude-really-do-with-your-a4b46bfb8294)
- [How to Stop AI Training on Your Data (Fello AI)](https://felloai.com/how-to-stop-ai-from-training-on-your-data/)
- [Anthropic Privacy Policy Update](https://www.anthropic.com/news/updates-to-our-consumer-terms)
- [Anthropic Privacy Center: Data Retention](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)
- [Anthropic Privacy Center: Training](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- [AI Chatbot Privacy Risks (Stanford)](https://news.stanford.edu/stories/2025/10/ai-chatbot-privacy-concerns-risks-research)

### Technical Concepts
- [AI Tokens Explained (NVIDIA Blog)](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- [LLM Temperature (IBM)](https://www.ibm.com/think/topics/llm-temperature)
- [Large Language Models (IBM)](https://www.ibm.com/think/topics/large-language-models)
- [Stochastic Parrot (Wikipedia)](https://en.wikipedia.org/wiki/Stochastic_parrot)

---

## Notes for L1 Content Development

### What to emphasize for beginners:
1. **All four major tools have free tiers** — no need to pay to start learning
2. **Privacy settings matter** — check them on day one
3. **AI is a tool, not an oracle** — always verify important information
4. **Different tools for different ecosystems** — Google users → Gemini, M365 users → Copilot, general use → ChatGPT or Claude
5. **Hallucinations are normal, not rare** — build the verification habit from day one

### What to avoid overwhelming beginners with:
- API pricing (irrelevant for L1)
- Model version numbers beyond "current" vs "previous"
- Technical architecture details
- Enterprise/Team plan specifics
- The philosophical debate about AI consciousness/understanding

### Key pricing insight:
All four major chatbots converge around $20/month for individual paid plans. The real differentiator is not price but ecosystem fit and feature focus.
