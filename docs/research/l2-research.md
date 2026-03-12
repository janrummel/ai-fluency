# L2 Research: Intentional Prompting

Working document for the AI Fluency L2 learning module. Research compiled 2026-03-12.

---

## 1. Prompt Anatomy: Role, Context, Task, Format, Constraints

All three major providers (Anthropic, OpenAI, Google) converge on the same core components of an effective prompt. The recommended structure is a 4-5 block pattern:

### The Five Components

| Component | What it does | Example |
|-----------|-------------|---------|
| **Role** | Sets the AI's persona, expertise, and tone | "You are a financial analyst specializing in SaaS metrics." |
| **Context** | Provides background information, situation, audience | "Our startup has 500 customers and just closed Series A. The board meeting is next week." |
| **Task** | The specific instruction — what to do | "Analyze our Q4 revenue data and identify the three biggest growth drivers." |
| **Format** | How the output should be structured | "Present as a table with columns: Driver, Revenue Impact, Confidence Level." |
| **Constraints** | Boundaries, limitations, what NOT to do | "Keep it under 300 words. Use plain language, no jargon. Do not speculate beyond the data." |

### Provider-Specific Guidance

**Anthropic (Claude):**
- Use XML tags to separate prompt sections: `<instructions>`, `<context>`, `<examples>`, `<output_format>`
- Place long documents ABOVE your instructions (Claude reads top-down)
- Use system prompt for role, user turn for task-specific instructions
- The "golden rule": show your prompt to a colleague — if they'd be confused, Claude will be too
- Source: [Anthropic Prompting Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)

**OpenAI (GPT):**
- Structure prompts for caching: static content first (system instructions, examples), variable content last (user query)
- For reasoning models (o1, o3, o4-mini): keep prompts simpler, don't add "think step by step" — they do it internally
- Pin production applications to specific model snapshots for consistency
- Source: [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

**Google (Gemini):**
- Gemini 3 favors directness over persuasion, logic over verbosity
- Shorter prompts often work better — start minimal, add detail only if needed
- Keep temperature at default 1.0; lowering it can cause unexpected behavior (looping)
- Use clear delimiters (XML tags or Markdown headings) consistently
- Source: [Google Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

### Cross-Provider Consensus

All three agree on these principles:
1. **Be specific** — vague instructions produce vague results
2. **Show, don't just tell** — examples are more effective than lengthy instructions
3. **One task per prompt** — multiple unrelated tasks confuse the model
4. **Specify output format** — tables, bullet points, length, tone
5. **Test and iterate** — treat prompt engineering as a science, not art

---

## 2. Prompting Techniques

### Zero-Shot Prompting

Give the model a direct instruction without any examples. Relies entirely on pre-trained knowledge.

**When to use:** Simple, well-understood tasks — basic questions, sentiment classification, straightforward formatting.

**Example:**
> "Classify the following customer review as Positive, Negative, or Neutral: 'The product arrived on time but the packaging was damaged.'"

### Few-Shot Prompting

Provide 2-5 examples of input-output pairs before the actual task. The model learns the pattern from the examples.

**When to use:** Complex formatting, specific tone/style, domain-specific classification, tasks where showing is easier than explaining.

**Example:**
> "Categorize these support tickets by priority:
>
> Ticket: 'Cannot log in to my account' -> Priority: High
> Ticket: 'How do I change my profile photo?' -> Priority: Low
> Ticket: 'Payment was charged twice' -> Priority: High
>
> Ticket: 'The dashboard loads slowly on mobile' -> Priority: ?"

**Important finding (2025 research):** For strong modern models, few-shot examples primarily enforce output FORMAT rather than improve reasoning. Zero-shot can match or exceed few-shot performance on reasoning tasks.

Source: [Few-Shot Prompting Guide](https://www.promptingguide.ai/techniques/fewshot)

### Chain-of-Thought (CoT) Prompting

Encourage the model to reason step-by-step before giving a final answer. Dramatically improves accuracy on complex tasks.

**Zero-Shot CoT** — Simply add "Think step by step" or "Let's work through this":
> "A company has 120 employees. 30% work remotely, and 15% of remote workers are in management. How many remote managers are there? Think step by step."

**Few-Shot CoT** — Show examples WITH the reasoning process:
> "Q: A store has 50 items. 20% are on sale, and half of sale items are under $10. How many sale items are under $10?
> A: Let me think step by step.
> - 20% of 50 = 10 items on sale
> - Half of 10 = 5 items under $10
> - Answer: 5
>
> Q: A team of 80 people has 25% senior members. 40% of seniors lead a project. How many seniors lead projects?"

Source: [Chain-of-Thought Prompting Guide](https://www.promptingguide.ai/techniques/cot)

### Role-Play Prompting

Assign a specific persona or expertise to the model. Steers the model toward language patterns, arguments, and formats associated with that role.

**Best practices:**
- Be specific: "You are a corporate tax attorney with 15 years of experience" beats "Act like a lawyer"
- Use direct phrasing ("You are...") rather than "Imagine you are..."
- Don't rely on role alone — combine with format constraints, audience, and examples
- Role prompting is most effective for domain-specific tone and vocabulary, not for factual accuracy

**Example:**
> "You are a senior product manager at a B2B SaaS company. A junior PM asks you: 'How should I prioritize features when we have too many requests?' Give practical, experience-based advice. Keep it to 5 actionable tips."

**Caveat:** Research is mixed on whether role prompting actually improves output quality. It reliably changes tone and vocabulary but does not always improve accuracy. Use it for style, not as a substitute for good instructions.

Source: [PromptHub: Role Prompting Analysis](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference)

---

## 3. Iteration as Method

Iterative prompting is a structured approach to refining AI outputs through repeated cycles of prompting, evaluating, and adjusting. Key principle: **don't expect a perfect answer on the first try.**

### The Iteration Cycle

1. **Draft prompt** — Write your initial prompt with role, context, task, format
2. **Evaluate output** — Check: Is the tone right? Is it the right length? Is it accurate? Is anything missing?
3. **Diagnose the gap** — Identify WHAT is wrong (not just "it's bad")
4. **Refine the prompt** — Make a specific adjustment targeting the gap
5. **Repeat** — Until the output meets your needs

### Practical Refinement Techniques

**Narrowing scope:**
- First prompt: "Write a marketing email for our new product"
- Refined: "Write a marketing email for our project management tool, targeting CTOs at companies with 50-200 employees. Emphasize the time-tracking feature. Keep it under 150 words."

**Adjusting tone:**
- Add: "Use a conversational but professional tone, similar to how Basecamp writes their blog posts"

**Adding constraints after seeing output:**
- "Good, but remove all bullet points and write it as flowing paragraphs"
- "This is too formal. Rewrite with shorter sentences and more direct language"

**Editing within conversation (dialogue refinement):**
- "Make the second paragraph more specific — include a concrete example"
- "The conclusion is weak. End with a clear call to action instead of a summary"
- "Keep everything but change the audience from executives to team leads"

### Key Insight

Iterative refinement is especially powerful because each follow-up prompt carries the context of the conversation. You don't need to rewrite the entire prompt — you can make surgical adjustments. This is a fundamentally different workflow from traditional tools.

Source: [IBM: What is Iterative Prompting?](https://www.ibm.com/think/topics/iterative-prompting), [Latitude: Iterative Prompt Refinement Guide](https://latitude.so/blog/iterative-prompt-refinement-step-by-step-guide)

---

## 4. Task Types with Prompt Examples

### Writing

> "You are a communications manager. Write an internal announcement email informing employees that the office will switch to a hybrid work model starting May 1. Tone: positive but factual. Include: the new schedule (3 days office, 2 days remote), who to contact with questions (HR), and that a FAQ document will follow. Keep it under 200 words."

### Analyzing

> "Here is our customer churn data for the past 6 months: [data]. Identify the top 3 factors correlated with churn. For each factor, explain the evidence, assess the confidence level (high/medium/low), and suggest one actionable intervention. Present your analysis as a table."

### Summarizing

> "Summarize the following 2,000-word article into 3 bullet points. Each bullet should be one sentence. Focus on: the main argument, the key evidence, and the practical implication for project managers. Write for someone who has 30 seconds to read this."

### Translating

> "Translate the following product description from English to German. Maintain the marketing tone — it should sound natural in German, not like a literal translation. Keep technical terms (API, SaaS, dashboard) in English. Target audience: German IT decision-makers."

### Brainstorming

> "I need to increase employee engagement in our quarterly all-hands meetings. Currently attendance is low and feedback is negative ('too long, too boring'). Generate 10 creative ideas to make these meetings more engaging. Mix practical/low-cost ideas with ambitious ones. For each idea, add one sentence on implementation effort (low/medium/high)."

### Coding (for non-developers)

> "Write an Excel formula that calculates the weighted average of cells B2:B10, where the weights are in cells C2:C10. Then explain in plain language what each part of the formula does, so I can adapt it for different ranges."

Source: [MIT Sloan: Effective Prompts for AI](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/), [Prompt Engineering Guide: Examples](https://www.promptingguide.ai/introduction/examples)

---

## 5. Good vs. Bad Prompts: Side-by-Side Comparisons

### Comparison 1: Vague vs. Specific

| Bad Prompt | Good Prompt |
|-----------|------------|
| "Write something about AI in healthcare." | "Write a 200-word summary of how AI is used in medical imaging diagnosis. Target audience: hospital administrators with no technical background. Include one real-world example and one limitation." |

**Why it matters:** The bad prompt forces the AI to guess the scope, length, audience, and angle. The good prompt eliminates all ambiguity. Result: fewer revisions, usable first draft.

### Comparison 2: No Context vs. Rich Context

| Bad Prompt | Good Prompt |
|-----------|------------|
| "Give me feedback on this email." | "I'm writing to a potential client who requested a proposal last week but hasn't responded. This is a follow-up email. The tone should be friendly but not pushy. Please review for: clarity, tone, and whether the call-to-action is strong enough. Here's the email: [text]" |

**Why it matters:** Without context, the AI gives generic writing tips. With context, it gives specific, actionable feedback tailored to the situation.

### Comparison 3: Multi-Task vs. Single-Task

| Bad Prompt | Good Prompt |
|-----------|------------|
| "Summarize this report, find the key insights, create a presentation outline, and draft talking points for the CEO." | "Based on this quarterly report, identify the 3 most important insights that the CEO should know. For each insight: state the finding in one sentence, provide the supporting data point, and rate the urgency (high/medium/low)." |

**Why it matters:** The bad prompt bundles 4 separate tasks. The AI tries to do everything and does nothing well. The good prompt focuses on one deliverable. You can tackle the presentation outline as a separate prompt using this output as input.

### Comparison 4: No Format Guidance vs. Clear Format

| Bad Prompt | Good Prompt |
|-----------|------------|
| "Compare these two project management tools." | "Compare Asana and Monday.com for a marketing team of 15 people. Use a table with these columns: Feature, Asana, Monday.com, Winner. Cover: task management, timeline view, integrations, pricing, learning curve. End with a one-paragraph recommendation." |

**Why it matters:** Format constraints prevent wall-of-text responses and make outputs immediately usable. The table format is directly paste-able into a presentation or document.

### Comparison 5: Assuming Knowledge vs. Providing Input

| Bad Prompt | Good Prompt |
|-----------|------------|
| "What should our content strategy be?" | "We're a B2B fintech startup (seed stage, 3 employees). Our target audience is CFOs at mid-size companies (100-500 employees). We currently publish nothing. Our goal is to generate 10 qualified leads per month within 6 months. Budget: $2,000/month. Suggest a content strategy with specific channel recommendations, content types, and a weekly publishing cadence." |

**Why it matters:** The AI cannot access your business context unless you provide it. The bad prompt gets a generic marketing textbook answer. The good prompt gets a tailored, actionable plan.

### Comparison 6: "Make It Better" vs. Targeted Feedback

| Bad Prompt | Good Prompt |
|-----------|------------|
| "This isn't good enough. Improve it." | "The tone is too formal for our audience (startup founders, 25-35 years old). Rewrite the first two paragraphs using shorter sentences and a more conversational style. Keep the data points but explain them like you're talking to a friend." |

**Why it matters:** "Improve it" gives the AI no direction — it might change things you liked. Targeted feedback tells the AI exactly what to fix and what to preserve. This is the difference between productive iteration and random changes.

Source: [eWeek: Good vs Bad ChatGPT Prompts 2026](https://www.eweek.com/news/10-good-vs-bad-chatgpt-prompts-2026/), [AI Tool Discovery: Prompt Engineering Guide](https://www.aitooldiscovery.com/guides/prompt-engineering), [Infomineo: Prompt Engineering Best Practices](https://infomineo.com/artificial-intelligence/prompt-engineering-techniques-examples-best-practices-guide/)

---

## Key Takeaways for Module Design

1. **The anatomy is universal** — Role/Context/Task/Format/Constraints works across all providers
2. **Few-shot is the most underused technique** by knowledge workers — it's simple and high-impact
3. **Iteration is the real skill** — treat AI interaction as a conversation, not a one-shot query
4. **Specificity wins** — every good-vs-bad comparison comes down to eliminating ambiguity
5. **Task-specific templates** are the most practical deliverable for learners
6. **Chain-of-thought is less relevant for knowledge workers** than for technical users — mention but don't over-emphasize
7. **Role prompting is overrated** in popular discourse — teach it as tone/style tool, not a magic lever

---

## All Sources

- [Anthropic: Prompting Best Practices (Claude 4)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- [Anthropic: Multishot Prompting](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
- [Anthropic: Prompt Engineering for Business Performance](https://www.anthropic.com/news/prompt-engineering-for-business-performance)
- [OpenAI: Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [OpenAI: Best Practices for Prompt Engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [OpenAI: GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)
- [Google: Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Google Cloud: Prompt Engineering Guide](https://cloud.google.com/discover/what-is-prompt-engineering)
- [Prompt Engineering Guide: Chain-of-Thought](https://www.promptingguide.ai/techniques/cot)
- [Prompt Engineering Guide: Few-Shot](https://www.promptingguide.ai/techniques/fewshot)
- [Prompt Engineering Guide: Examples](https://www.promptingguide.ai/introduction/examples)
- [Learn Prompting: Zero-Shot CoT](https://learnprompting.org/docs/intermediate/zero_shot_cot)
- [Learn Prompting: Role Prompting](https://learnprompting.org/docs/advanced/zero_shot/role_prompting)
- [IBM: The 2026 Guide to Prompt Engineering](https://www.ibm.com/think/prompt-engineering)
- [IBM: What is Iterative Prompting?](https://www.ibm.com/think/topics/iterative-prompting)
- [MIT Sloan: Effective Prompts for AI](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/)
- [Lakera: Ultimate Guide to Prompt Engineering 2026](https://www.lakera.ai/blog/prompt-engineering-guide)
- [PromptHub: Role Prompting Analysis](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference)
- [Latitude: Iterative Prompt Refinement Guide](https://latitude.so/blog/iterative-prompt-refinement-step-by-step-guide)
- [eWeek: Good vs Bad ChatGPT Prompts 2026](https://www.eweek.com/news/10-good-vs-bad-chatgpt-prompts-2026/)
- [Infomineo: Prompt Engineering Best Practices](https://infomineo.com/artificial-intelligence/prompt-engineering-techniques-examples-best-practices-guide/)
- [Philipp Schmid: Gemini 3 Prompt Practices](https://www.philschmid.de/gemini-3-prompt-practices)
- [arXiv: Revisiting Chain-of-Thought Prompting (2025)](https://arxiv.org/abs/2506.14641)
