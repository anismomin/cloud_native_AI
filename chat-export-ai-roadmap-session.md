# Chat Export — AI Engineer Roadmap Planning Session

**Date:** July 17, 2026
**Participants:** Shakil (user) & Claude
**Purpose of this export:** Context file to reuse in future AI sessions. The two full roadmap documents were delivered separately and are **not duplicated here** — only referenced.

**Deliverables produced in this chat (saved separately):**
1. `ai-engineer-roadmap.md` — Laravel/PHP-first AI Engineer roadmap (6 phases)
2. `ai-agents-python-roadmap.md` — Python + Agent Factory baby-steps roadmap (Steps 0–8, with validation exercises + marketing/monetization section)

---

## Turn 1 — Initial Request

**Shakil:**
> I am fullstack developer. Have over a decade experience building websites, SaaS products, managing DevOps. Working full time mostly on Laravel; experience building apps in React, Laravel, Next.js, NestJS etc. Currently doing coding using AI. I am eager to become an AI engineer. Plan a roadmap for me with resources to adapt AI. Each step should bring some expertise to my toolbox which I can use in my daily work. Create a markdown for the plan.

**Claude — response summary:**
Created **`ai-engineer-roadmap.md`** (Doc 1). Key framing and structure:

- **Core bet:** Shakil is already ~70% of an AI engineer — AI engineering is mostly APIs, queues, retries, DevOps. His Laravel/Postgres/infra stack is an asset.
- **6 phases over ~6–9 months** (5–8 hrs/week), each ending in a shippable build usable in agency work:
  - **Phase 0 — Mindset:** AI Engineering ≠ ML research; API-first. (swyx's "Rise of the AI Engineer", applied-llms.org)
  - **Phase 1 — LLM APIs & Prompt Engineering:** structured outputs, streaming, few-shot/CoT; Laravel tools: openai-php, Prism. Build: email summarizer or contact-form data extractor.
  - **Phase 2 — Embeddings & RAG:** pgvector-first (already runs Postgres), chunking, hybrid search, citations. Build: "chat with our docs."
  - **Phase 3 — Tool Use, Agents & MCP:** agent loop, MCP servers, guardrails. Build: MCP server exposing a Laravel app; lead-triage agent with human approval.
  - **Phase 4 — Evals & Observability:** golden datasets, LLM-as-judge, Langfuse, promptfoo in CI, prompt caching, cost routing, OWASP LLM Top 10. "This separates AI engineers from demo builders."
  - **Phase 5 — Open Models & Fine-tuning (optional):** Ollama, vLLM, LoRA/Unsloth; privacy pitch for healthcare clients; DevOps advantage for self-hosting.
  - **Phase 6 — Ship & Position:** public projects, agency AI service line, Latent Space + Simon Willison for staying current.
- Included a skill self-assessment checklist and guiding principles (evals as unit tests; build in his healthcare/B2B niche).

---

## Turn 2 — Pivot to Python + Agent Factory, Baby Steps

**Shakil:**
> It's mainly around Laravel but I want another one — with Python, as I took some courses for Python and RAG; I even built a RAG for a client using AI coding. I am not a bookworm; I mostly learn by practice and courses. I wanted to learn this Agent Factory stuff (https://agentfactory.panaversity.org/docs/about) but it's large to adapt — make it in baby steps so I can adapt it into my daily life. #AIAgents #AIWorkflows #AIEmployees. Create another separate doc with these additional points.

**Claude — response summary:**
Fetched the Panaversity Agent Factory site and created **`ai-agents-python-roadmap.md`** (Doc 2). Key points:

- **Agent Factory context (from their docs):** teaches building "Digital FTEs" / AI Workers via spec-driven, human-supervised development; the 10-80-10 rule (human sets direction 10% → AI executes 80% → human verifies 10%); ladder = Foundations → Mode 1 (use agents for your own work) → Mode 2 (manufacture AI Workers) → scale to AI-Native Company; top role = Forward Deployed Engineer (FDE); tools: Claude Code / OpenCode, SKILL.md format, MCP, one-Postgres architecture (relational + full-text + pgvector together); Python SDK of choice: OpenAI Agents SDK.
- **Mapping to Shakil:** Foundations mostly done, Mode 1 needs formalizing, Mode 2 is the goal. Roadmap never reads the whole book — each step names exactly ONE Agent Factory crash course.
- **Steps (1–2 weeks each, 45–60 min/day):**
  - **Step 0:** Python AI stack — uv, Pydantic structured outputs, FastAPI, OpenRouter. Pydantic outputs ≈ "Laravel Form Requests for LLMs."
  - **Step 1:** Formalize Mode 1 — agentic coding, spec-driven development, first SKILL.md used on real agency work.
  - **Step 2:** First real agent — build raw agent loop by hand (~80 lines) so it's never magic, THEN OpenAI Agents SDK. Build: lead-qualifier agent.
  - **Step 3:** Workflows (#AIWorkflows) — Anthropic's 5 patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer); workflow vs agent vs plain-code decision framework. Build: agency content pipeline with brand-voice evaluator.
  - **Step 4:** Level up existing RAG — Postgres/pgvector hybrid search + reranking; RAG becomes a TOOL agents call, not an app.
  - **Step 5:** MCP — build own server with FastMCP/Python SDK. Build: "11th Agency MCP" (list_projects, get_client_brief, create_invoice_draft).
  - **Step 6:** First AI Employee / Digital FTE (#AIEmployees) — spec first; trigger (cron/queue/webhook) + MCP tools + Postgres memory + human-approval gate; Docker on VPS. Build options: inbox-triage FTE or lead-follow-up FTE.
  - **Step 7:** Evals + observability — Eval-Driven Development, Langfuse (self-hosted), promptfoo/pytest in CI, guardrails, prompt-injection defense.
  - **Step 8:** Scale & position — multi-worker handoffs, productize, publish case studies, FDE path ("your agency job with a new title").
- **Baby-steps rules:** one crash course per step; every step ships running code; use each skill at work within 7 days; workflows before agents before employees; Python for AI / PHP for everything else (Laravel apps become tools agents call); spec first always.
- Progress checklist included.

---

## Turn 3 — Add Validation Exercises

**Shakil:**
> Also add a small project or exercise to validate my skills on every step.

**Claude — response summary:**
Updated Doc 2: every step now has a **✅ Validation exercise** with explicit pass conditions, plus the checklist gained a second "Validated" column (rule: don't advance until both Built + Validated are checked). The exercises:

- **Step 0 — Invoice Parser:** 3 messy invoices → validated Pydantic model; must handle one garbage input gracefully.
- **Step 1 — Spec Rematch:** rebuild a vibe-coded feature from a written spec in a fresh session; pass = ≤2 correction prompts + a second SKILL.md that works on first load.
- **Step 2 — Whiteboard Test:** rebuild agent loop from memory, docs closed, 2 tools; must chain tools to answer a compound question and stop on its own.
- **Step 3 — Triage Quiz + Router:** label 6 real agency tasks (code/workflow/agent) + build a classifier-router; 9/10 routing accuracy.
- **Step 4 — Break Your Own RAG:** 10 questions incl. 2 trap questions the docs can't answer; pass = ≥8/10 correct with citations AND "I don't know" on traps (no hallucination) AND one case where hybrid beats pure vector.
- **Step 5 — One Server, Two Clients:** same MCP server drives Claude Desktop AND own Python agent; clean recoverable errors; 60-second non-dev explanation; bonus: add a resource (not just tools).
- **Step 6 — 5-Day Probation:** FTE runs 5 working days; pass = zero manual restarts, approval gate catches 100% of irreversible actions, ≥60% zero-edit drafts, one correctly-refused boundary. Failures become the Step 7 eval dataset.
- **Step 7 — Regression Trap:** deliberately sabotage the FTE prompt; evals must catch the regression before manual review would; answer cost/latency/prompt questions in Langfuse in <2 min; one prompt-injection attempt must be blocked.
- **Step 8 — Handoff + Pitch:** Worker A → Worker B handoff end-to-end with full trace; pitch one worker as a 1-pager to a real person; pass = someone says "I'd pay for that" or explains exactly why not.

---

## Turn 4 — Add Marketing, Monetization & Career

**Shakil:**
> Also add how to market myself and monetize based on my new skills in a way I advance in a career.

**Claude — response summary:**
Added a **"Market Yourself & Monetize"** section to Doc 2, running in parallel with the learning steps:

- **Three lanes at once:** (A) agency services via 11th Agency — fastest money; (B) freelance/consulting — independent proof; (C) job market (AI Engineer/FDE roles) — highest ceiling.
- **Positioning statement (unfair advantage):** "I build AI agents and workflows that plug into real business systems — backed by 10+ years shipping production web apps, and an agency track record with healthcare, B2B, and SaaS brands." Most AI freelancers can't deploy/maintain; most senior devs can't build agents.
- **Step-by-step monetization map (rough ranges):**
  - Step 2–3 → AI Workflow Audit: $500–$2,500 fixed fee
  - Step 3 → single workflow build: $1,500–$5,000
  - Step 4 → private "chat with your docs" on client's own Postgres (privacy pitch for healthcare): $3,000–$10,000 + hosting retainer
  - Step 5 → MCP integrations (CRM/WordPress/HubSpot/EHR): $2,000–$8,000
  - Step 6 → **AI Employee retainers: $500–$3,000/mo per worker** ← the key move: projects = one-time money; workers + reliability = recurring money
  - Step 7 → AI reliability retainer (evals/monitoring/cost): $1,000–$5,000/mo
  - Step 8 → FDE-style engagements: $5k–$15k/mo or salaried
- **Proof > claims:** one 60–90s demo clip per validated step; case-study formula (problem → build + diagram → demo → measurable result → stack); 2–3 clean GitHub repos; hashtag posts (#AIAgents #AIWorkflows #AIEmployees) WITH demos, weekly from Step 2; "numbers or it didn't happen" (e.g., "47 replies drafted, 68% zero-edit, $0.03/run").
- **Money sources in order of ease:** (1) existing clients — free 30-min automation audit → paid build → retainer; (2) agency's own operations as public demos; (3) freelance platforms — proposals lead with production/DevOps/evals/approval-gate language hobbyists never use; (4) white-label agent builds for other agencies; (5) job market — new resume tier: AI Engineer, AI Solutions Engineer, Agent Engineer, Applied AI Engineer, FDE, GenAI Developer, with XYZ-formula bullets sourced from validation exercises.
- **Career ladder:** L1 (mo 1–3) AI-augmented senior dev → L2 (3–6) AI integration specialist → L3 (6–9) AI Engineer with FTEs on retainer → L4 (9+) FDE / productized "agency that ships AI employees."
- **Business validation gates (added to checklist as 💰 rows):** client AI deliverable by Step 3; first monthly retainer + updated resume by Step 6; 3 case studies + 1 recurring client + 1 interview/contract conversation by Step 8. Rule: if money isn't appearing, it's usually visibility, not skill — double demo posts before doubling study hours.

---

## Key Context for Future Sessions (TL;DR)

- **Profile:** Shakil — fullstack dev, 10+ yrs, Laravel-primary (also React/Next.js/NestJS), DevOps, runs 11th Agency (B2B/SaaS/healthcare/wellness clients), codes with AI daily, took Python + RAG courses, already shipped a client RAG via AI coding. Learns by practice/courses, not books. Wants baby steps that fit daily life.
- **Goal:** Become an AI Engineer → build #AIAgents, #AIWorkflows, #AIEmployees (Digital FTEs), following the Panaversity Agent Factory method, with monetization/career advancement along the way.
- **Chosen stack (Doc 2):** Python (uv, Pydantic, FastAPI), OpenAI Agents SDK, Postgres + pgvector (hybrid search), FastMCP/MCP Python SDK, Langfuse + promptfoo, Docker/VPS deploy. PHP/Laravel apps become tools that agents call.
- **Current position on the ladder:** Foundations ✅ done → Mode 1 🟡 formalizing → Mode 2 🎯 target → FDE 🚀 ceiling.
- **Operating rules:** one crash course per step; ship every step; apply at work within 7 days; workflows → agents → employees in that order; spec-first (10-80-10); don't advance until Built + Validated both checked; monetize in parallel per the 💰 gates.
- **Next action when resuming:** check which step of `ai-agents-python-roadmap.md` is in progress, review its validation exercise status, and continue from there.
