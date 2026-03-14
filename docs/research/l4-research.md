# L4 Research: AI as Coworker

Working document for the AI Fluency L4 learning module. Research compiled 2026-03-14.

Research is split across multiple files for this level:

## Research Files

1. **Enterprise Case Studies & Delegation Frameworks** → `ai-as-coworker-research.md`
   - HBS/BCG productivity study (758 consultants, 40% quality boost)
   - Klarna, Zapier, DoorDash, Intercom case studies
   - Failure cases (Air Canada, legal hallucinations, McDonald's)
   - Trust calibration frameworks (CSA Intern/Junior, TCMM)
   - Delegation spectrum (5-level autonomy, Centaur/Cyborg model)
   - McKinsey $4.4T opportunity, Deloitte State of AI 2026

2. **Claude Cowork** → Agent output (consolidated below)
   - Desktop agent, containerized Linux VM, local file access
   - 38+ MCP connectors (Gmail, Drive, Slack, etc.)
   - Scheduled Tasks (hourly to weekly)
   - Pro $20/mo, Max $100-200/mo, Team Premium $100-125/mo
   - Safety: folder sandboxing, prompt injection risk acknowledged
   - Cross-app workflows (Excel + PowerPoint)

3. **ChatGPT Agent Mode** → Agent output (consolidated below)
   - Unified: Operator + Deep Research + ChatGPT core
   - Cloud-based (no local file access)
   - Visual + text browser, terminal, file system, apps/connectors
   - Scheduled Tasks (up to 10 active)
   - Plus $20/mo (40 msg), Pro $200/mo (400 msg)
   - Safety: user confirmations, watch mode, browser sandbox

4. **EU AI Act** → Agent output (consolidated below)
   - Risk-based: unacceptable → high → limited → minimal
   - AI Literacy obligation since Feb 2025 (Art. 4)
   - Transparency obligations from Aug 2026 (Art. 50)
   - Human oversight required for high-risk (Art. 14)
   - Agentic AI not explicitly defined — risk depends on use case
   - Deployer (employer) liable, not end user
   - Fines up to 35M EUR / 7% global revenue

## Key Comparisons

### Claude Cowork vs ChatGPT Agent

| Dimension | Claude Cowork | ChatGPT Agent |
|-----------|--------------|---------------|
| Focus | Desktop/local files | Web-based tasks |
| Environment | Local (containerized VM) | Cloud (virtual browser) |
| Local files | Yes (folder sandbox) | No |
| Web browsing | Chrome extension | Visual + text browser |
| Scheduled tasks | Yes (needs app open) | Yes (up to 10) |
| Sub-agents | Yes (parallel) | No |
| Entry price | $20/mo (Pro) | $20/mo (Plus) |
| Best for | Document creation, file work | Web automation, research |

### Delegation Spectrum (from research)

| Level | User Role | Agent Behavior | Example |
|-------|-----------|----------------|---------|
| L0 | Operator | Fully user-directed | ChatGPT Q&A |
| L1 | Collaborator | AI suggests, user decides | Copilot suggestions |
| L2 | Consultant | AI works on subtasks independently | Background research |
| L3 | Approver | AI proposes, user approves | AI drafts, user sends |
| L4 | Observer | AI acts autonomously | Autonomous agents |

### Trust Calibration (CSA Framework)

| Trust Level | Analogy | Permissions | Oversight |
|-------------|---------|-------------|-----------|
| Intern | New hire | Read-only, observe | Constant |
| Junior | Junior employee | Recommend, needs approval | Regular review |
| Senior | Senior employee | Execute with monitoring | Exception-based |
| Expert | Trusted expert | High autonomy | Spot checks |
