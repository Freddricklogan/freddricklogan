# Portfolio Modernization Blueprint

**Portfolio:** github.com/Freddricklogan · 49 shipped projects across five categories
**Audience:** CTOs, VP-level hiring managers, technical due-diligence teams, enterprise consulting prospects
**Rule zero:** no existing URL changes. Every repo name and every `freddricklogan.github.io/<repo>/` path stays exactly as it is.

---

## 0. Where the portfolio stands today (measured, September 2026)

All 49 repositories were cloned and inspected.

| Finding | Count | Consequence for an executive reviewer |
|---|---|---|
| Single-file `index.html` demos (vanilla JS + CDN Chart.js/D3/Plotly) | 33 | Look like class projects; no tests, no CI, unpinned CDN, no CSP |
| Python scripts/notebooks (pandas, scikit-learn, TensorFlow) | 9 | No packaging, no tests, no reproducible environment |
| Real backend service (Flask 3 + SQLite) | 1 | Hard-coded default API key, key accepted in query string, no tests |
| Infrastructure as code (Terraform, AWS three-tier) | 1 | Unpinned providers, no scanning, no remote state |
| Docs-only frameworks/playbooks (policy, ethics, transformation) | 4 | Strong thought leadership, zero engineering signal |
| Jekyll course site | 1 | Fine as-is; needs the shared README standard |
| Repos with any GitHub Actions workflow | **0** | No CI/CD signal anywhere |
| Repos with any automated test | **0** | No quality signal anywhere |
| Repos with a LICENSE file | 24 | Half the portfolio is legally ambiguous to reuse |

The good news: the *ideas* are principal-level (RK4 epidemic solvers, Monte Carlo VaR, MITRE ATT&CK mapping, verifiable credentials, Well-Architected review automation). The gap is entirely in engineering rigor and presentation — which is the cheapest gap to close.

### What has already been delivered in this pass (reference implementations)

| Repo | What changed | Measured result |
|---|---|---|
| `student-engagement-api` | Flask → FastAPI + Pydantic v2, hexagonal layout, OAuth2/JWT RBAC, RFC 9457 errors, structlog + correlation IDs, rate limiting, Docker, CI, Scalar API explorer, 43-item audit | **146 tests, 98 % coverage**, ruff/mypy-strict/bandit/pip-audit clean |
| `siem-log-analyzer` | ES-module refactor, Executive Shell, CSP + SRI, Vitest, CI, 30-item audit (12 real logic bugs fixed, incl. a `Math.random()` threat score) | **95 tests, 99.8 % coverage**, Playwright smoke pass |
| `verifiable-academic-credentials` | Real `did:key` (P-256 multicodec), bitstring status list, ES modules, Executive Shell, Vitest, CI, 29-item audit (9 crypto-soundness defects fixed) | **133 tests, 99.3 % coverage**, Playwright smoke pass |
| `aws-terraform-gameday` | Module split (network/compute/alb/observability), pinned versions, IMDSv2, encryption, flow logs, `terraform test` suites, Checkov/Trivy CI, facilitator guide, Game Day console page | **Checkov 148 pass / 0 fail** (was 28 / 20) |
| `_kit/static-demo` | Reusable Executive Shell (CSS + JS), README template, CI templates, 60-minute conversion checklist | Applies to the remaining 31 static demos |

---

## SECTION 1: Portfolio Modernization Matrix

**Tiers.** *T1 Flagship* — full refactor, deep README, live demo, first thing a CTO opens. *T2 Showcase* — Executive Shell + tests + CI via the kit. *T3 Consolidate* — merge into a parent repo or archive with a one-paragraph README so it stops diluting the signal. Consolidation never deletes a URL: the old repo stays, gets an archive banner, and links forward.

**Demo strategy legend.** *Pages* = GitHub Pages via `actions/deploy-pages` (zero cost, zero ops). *Pages+Worker* = static UI on Pages with a Cloudflare Worker for any server-side piece (free tier). *Container* = Render/Fly free tier from the repo's Dockerfile. *Streamlit* = Streamlit Community Cloud for notebook-style ML.

### I. Data Architecture & Machine Learning (16)

| Repo | Current stack | Modernization & tech injection | Competencies | Demo | Tier |
|---|---|---|---|---|---|
| neural-network-playground | Vanilla JS, Canvas, Chart.js | TypeScript + Vite; move training to a Web Worker with WebGPU fallback (`@tensorflow/tfjs` optional); export ONNX; Vitest on layer math | ML fundamentals, numerical computing, UX for explainability | Pages | T1 |
| epidemic-modeling-dashboard | JS, Chart.js, RK4 | TypeScript; adaptive-step RK45; parameter sweeps in Worker; scenario export; unit tests against closed-form SIR limits | Scientific computing, simulation, decision support | Pages | T1 |
| monte-carlo-simulator | JS, Chart.js, Web Workers | TypeScript; quasi-random (Sobol) option; variance-reduction demo; Vitest with statistical tolerance tests | Quant methods, parallelism, numerical accuracy | Pages | T2 |
| fintech-risk-analytics | JS, Plotly | TypeScript; historical + parametric + MC VaR side-by-side; Black-Scholes Greeks; CSV import; tests vs. known values | Risk analytics, model validation | Pages | T2 |
| DeepLearning-Charity | TensorFlow/Keras, notebooks | Package as `src/` + `pyproject`; PyTorch Lightning or Keras 3; MLflow tracking; model card; pytest on preprocessing; Dockerfile | MLOps, data governance, evaluation | Streamlit | T2 |
| SentimentAnalysis-System | Python, Flask, NLP | FastAPI + Pydantic v2; swap to a small transformer (DistilBERT) via `transformers`; batch endpoint; eval harness with F1 reported; Docker | NLP, API design, evaluation | Container | T2 |
| Crypto-Clustering | scikit-learn, PCA | Package + pytest; add HDBSCAN comparison; silhouette/DBI metrics; interactive Plotly export to Pages | Unsupervised learning, feature engineering | Streamlit or Pages | T2 |
| MedicalTreatment-Analytics | pandas, matplotlib | Package + pytest; statsmodels for proper survival/ANOVA; reproducible `make report`; data-provenance note | Statistics, reproducibility, data ethics | Pages (static report) | T3 |
| earthquake-visualization | Leaflet, D3, package.json | TypeScript; live USGS GeoJSON feed with caching Worker; clustering; accessibility pass | Geospatial, real-time data | Pages+Worker | T2 |
| belly-button-challenge | D3, Plotly | Executive Shell + kit CI; keep scope | Data viz | Pages | T3 |
| UFO-Sightings | D3 | Executive Shell + kit CI; keep scope | Data viz, filtering | Pages | T3 |
| WebScraping-Mars | Flask, BeautifulSoup, MongoDB | Convert to a scheduled GitHub Action that scrapes to JSON + static Pages dashboard (no Mongo to host) | Data pipelines, automation | Pages (Action-fed) | T3 |
| Financial-Analysis, PyBank | Python scripts | **Consolidate** into `python-data-fundamentals` with a tested CLI (`typer`), keep old repos as archived pointers | Fundamentals | none | T3 |
| PyPoll, Election-Analysis | Python scripts | **Consolidate** into the same fundamentals repo | Fundamentals | none | T3 |

### II. Cloud Infrastructure & Security (9)

| Repo | Current stack | Modernization & tech injection | Competencies | Demo | Tier |
|---|---|---|---|---|---|
| siem-log-analyzer | JS, Chart.js | **Done** (ES modules, Sigma-style rule engine, ATT&CK mapping, tests, CI). Next: Sigma rule import, OpenTelemetry log format, optional Rust/WASM parser for 1M-line files | SecOps, detection engineering, threat modeling | Pages | T1 ✅ |
| cloud-architecture-designer | JS, Canvas | TypeScript; export to Terraform/CloudFormation skeleton; Well-Architected checks as testable rules; Vitest | Enterprise architecture, IaC | Pages | T1 |
| aws-terraform-gameday | Terraform | **Done** (modules, tests, Checkov/Trivy CI, console). Next: OPA/Conftest policy pack, Infracost in PR | Platform engineering, IaC security, EdTech (Game Day pedagogy) | Pages console; no live AWS | T1 ✅ |
| cybersecurity-incident-dashboard | JS, Chart.js, D3 | TypeScript; STIX 2.1 import; incident timeline with ATT&CK navigator layer export; kit CI | SecOps, incident response | Pages | T2 |
| network-vulnerability-scanner | JS, Chart.js | Rename nothing; add a real scanner backend as a *separate* Go microservice (`nmap`-free, TCP connect + banner) deployable as a container, static UI stays on Pages with sample data; CVE lookup via NVD API cached in a Worker | Security engineering, Go, API design | Pages + optional container | T2 |
| encryption-toolkit | JS, Web Crypto | TypeScript; Vitest against NIST test vectors; add HKDF, AES-GCM AAD, key wrapping; remove "steganography" claim unless implemented properly | Applied cryptography | Pages | T2 |
| serverless-workflow-simulator | JS, Chart.js | TypeScript; import real AWS Step Functions ASL; cost model from public price list JSON; tests | Cloud economics, event-driven design | Pages | T2 |
| cloud-cost-optimizer | JS, Chart.js | TypeScript; FinOps FOCUS-format CSV import; right-sizing rules as tested functions | FinOps, data governance | Pages | T2 |
| secure-password-generator | JS, Web Crypto | Kit CI + tests (entropy calc); keep scope | Crypto hygiene | Pages | T3 |

### III. Educational Technology Systems (12)

| Repo | Current stack | Modernization & tech injection | Competencies | Demo | Tier |
|---|---|---|---|---|---|
| student-engagement-api | Flask, SQLite | **Done** (FastAPI, RBAC, 98 % coverage). Next: Postgres profile in prod, OpenTelemetry traces, xAPI/Caliper ingest | Backend architecture, security, learning analytics | Container (Render/Fly one-click) | T1 ✅ |
| verifiable-academic-credentials | JS, Web Crypto | **Done** (did:key, status list, tests). Next: W3C VC-JWT + Open Badges 3.0 export, QR verify flow | Digital credentials, PKI, standards | Pages | T1 ✅ |
| edtech-program-command-center | JS | TypeScript; Executive Shell; cohort/outcome model with tested KPI math; CSV import | Program leadership, analytics | Pages | T1 |
| Education-Leadership-Dashboard | HTML/JS | Kit conversion; merge data model with command center where sensible | Decision support | Pages | T2 |
| Educational-LMS-Prototype | HTML/JS | Kit conversion; add LTI 1.3 launch *simulator* and WCAG audit report | LMS architecture, accessibility | Pages | T2 |
| Remote-Education-Toolkit | HTML/JS | Kit conversion; PWA (offline) | Human-centered design | Pages | T2 |
| tech-enhanced-learning | Jekyll | README standard + Pages workflow; keep | Instructional design | Pages | T3 |
| Government-Service-Portal | HTML/JS | Kit conversion; USWDS-aligned components; accessibility report | Service design, accessibility | Pages | T2 |
| Blockchain-Educational-Credentials | src + paper | Fold code into verifiable-academic-credentials as an "anchoring" module; keep repo as the research/paper home with archive banner | Research translation | none | T3 |
| EdTech-Policy-Framework | docs | Convert to a Docusaurus/MkDocs site on Pages with a policy-checklist tool | Governance | Pages | T3 |
| AI-Ethics-Education-Framework | docs + templates | MkDocs site + interactive risk-assessment worksheet (ties to Flagship 2) | AI governance | Pages | T3 |
| Public-Service-Digital-Transformation | docs + templates | MkDocs site; playbook as maturity-model calculator | Change management | Pages | T3 |

### IV. Interactive Learning Resources (10)

qualitative-research-methods · quantitative-inquiry · educational-policy-analysis · educational-leadership · higher-education-leadership · global-higher-education · teaching-and-teacher-education · museums-informal-learning · online-course-design · accessibility-udl

| Current stack | Modernization & tech injection | Competencies | Demo | Tier |
|---|---|---|---|---|
| Single `index.html` each | One shared **`learning-resource-kit`** (TypeScript, Executive Shell, quiz engine with xAPI statements, progress in localStorage, print stylesheet); each repo becomes content + config, CI from the kit; a hub page already exists at `/resources/` | Educational design, content architecture, accessibility (UDL) | Pages | T2 (batch) |

### V. Developer Tooling (2)

| Repo | Current stack | Modernization & tech injection | Competencies | Demo | Tier |
|---|---|---|---|---|---|
| cli-development-tools | Node + Python scripts | TypeScript + `commander`, single `npm i -g`, Vitest, `npm publish` dry-run in CI, SBOM via CycloneDX | Developer experience, supply-chain hygiene | npm badge + asciinema | T2 |
| python-utilities | Python scripts | `typer` CLI package, pytest, `pipx` install; or consolidate into fundamentals repo | Fundamentals | none | T3 |

**Net effect of the tiering:** 8 flagships a reviewer actually opens, ~25 showcase repos that all look identical in quality, ~16 consolidated/archived so nothing on the profile looks abandoned.

---

## SECTION 2: Flagship Projects

### 2A. Three convergence flagships

#### Flagship 1 — **Bastion Range**: enterprise security learning sandbox (Cybersecurity + EdTech + CS)

**Executive pitch.** Security teams buy tabletop exercises and CTFs that teach attack, not defense. Bastion Range emulates adversary behavior against a disposable environment and scores the *defender's* response in real time — mapped to MITRE ATT&CK and NIST CSF — so a CISO can show measurable detection-and-response improvement per analyst per quarter. Business problem: mean-time-to-detect is a board metric, but training spend has no line of sight to it.

**Architecture & stack.**
- Control plane: Go (chi) API + Postgres; scenario definitions as YAML validated by JSON Schema.
- Adversary emulation: Caldera-style ability library executed by a Rust agent inside ephemeral Firecracker/Kata containers (Docker Compose for the demo, K8s Jobs for scale).
- Telemetry: OpenTelemetry Collector → ClickHouse; eBPF sensor (Tetragon or a small Aya program) for process/network events.
- Detection feedback: Sigma rules evaluated in-stream; scoring service computes time-to-detect, false-positive rate, containment latency.
- UI: Next.js 15 / React 19 / TypeScript, server actions, live dashboard over SSE.
- Security: zero-trust between services (mTLS via SPIFFE/SPIRE), per-tenant network policies, signed scenario bundles (cosign).
- Pedagogy: mastery-based progression (Bloom-aligned objectives per scenario), hints that cost points, after-action report auto-generated.

**Core algorithms & pipelines.** Attack-graph generation from ATT&CK technique dependencies (topological sort with randomized branch selection); detection scoring as a survival curve (Kaplan-Meier over detect events) so partial credit is principled; Bayesian knowledge tracing per technique for the learner model.

**Milestones.** (1) Scenario schema + 5 ATT&CK techniques emulated in Compose, detection via Sigma over OTel logs — 3 weeks. (2) Scoring service + after-action report + Next.js dashboard — 3 weeks. (3) eBPF sensor + ClickHouse + SSE live view — 3 weeks. (4) SPIFFE mTLS, signed bundles, multi-tenant, K8s Job runner — 3 weeks. (5) Learner model + 20 scenarios + facilitator mode — 3 weeks.

**Live demo.** "Watch a breach in 60 seconds": a public read-only replay of a recorded scenario — attack timeline on the left, detections lighting up on the right, score ticking — hosted as static replay on Pages; a full sandbox runs via `docker compose up` with a seeded demo tenant.

#### Flagship 2 — **Sentinel Ledger**: AI/ML model auditing & telemetry platform (Data Science + Cybersecurity + Technologist)

**Executive pitch.** Enterprises are shipping LLM features faster than they can prove they are safe. Sentinel Ledger sits on the wire between applications and models, detecting prompt injection, PII leakage, data drift and poisoning signals, and producing an audit trail that satisfies the EU AI Act / NIST AI RMF paperwork the CIO is about to be asked for. Business problem: one leaked customer record or one jailbreak screenshot costs more than the whole ML program.

**Architecture & stack.**
- Gateway: Rust (axum + tower) reverse proxy adding < 2 ms p50 (design target) — streaming-aware, compatible with the common chat-completion API shapes.
- Detectors as WASM plugins (Extism): prompt-injection classifier (DeBERTa-small distilled to ONNX), PII (Presidio-style recognizers + regex + checksum validators), canary tokens, embedding-drift monitor (PSI/KS on embedding PCA components), output toxicity.
- Telemetry: OpenTelemetry traces with model-specific semantic conventions → Tempo/ClickHouse; Grafana dashboards or a Next.js console.
- Storage: append-only audit log with hash chaining (Merkle root published daily) — tamper-evident like the credentials repo.
- Model ops: vLLM for the local judge model; PyTorch for detector training; MLflow registry; evaluation harness with labelled attack corpora.
- Zero-trust: per-app API keys with scopes, policy-as-code (OPA/Rego) per route, secrets from Vault/SOPS.

**Core algorithms & pipelines.** Two-stage injection detection (cheap heuristics → ONNX classifier, budgeted by latency); PII redaction with reversible tokenization (format-preserving encryption, FF3-1) so downstream analytics keep working; drift via population stability index on sliding windows with Page-Hinkley change detection; poisoning signal via influence-function approximation on fine-tune batches.

**Milestones.** (1) Rust proxy + OTel + hash-chained audit log — 3 weeks. (2) PII and injection detectors as WASM, eval harness with precision/recall reported — 4 weeks. (3) Drift/poisoning monitors + Grafana/Next.js console — 3 weeks. (4) OPA policies, key scopes, Vault — 2 weeks. (5) Compliance report generator (AI RMF / ISO 42001 mapping) — 2 weeks.

**Live demo.** "Try to break it": a public playground where a reviewer types a prompt, sees the detector verdicts, redactions and latency budget in real time against a small local model — Pages UI calling a Fly-hosted gateway with strict rate limits; one-click "replay 10 famous jailbreaks" button.

#### Flagship 3 — **Atlas Tutor**: adaptive multimodal learning engine (EdTech + Data Science + Distributed Systems)

**Executive pitch.** Institutions want AI tutoring without shipping student data to a vendor. Atlas Tutor is a self-hostable RAG tutor with a knowledge-graph skill model: it knows what a learner has mastered, generates assessments aligned to specific objectives, and runs on a single GPU node or a laptop. Business problem: retention and time-to-competency are the metrics that fund programs like Elevate; generic chatbots move neither.

**Architecture & stack.**
- Services (Go or Python/FastAPI, gRPC between them): ingestion (PDF/video/slides → chunks + transcripts via Whisper), retrieval (pgvector or Qdrant, hybrid BM25 + dense, reranker), tutor (local LLM via vLLM/Ollama with structured outputs), assessment generator, learner-model service.
- Knowledge graph: Neo4j or Postgres + Apache AGE; skills as nodes with prerequisite edges; Bayesian Knowledge Tracing / Deep Knowledge Tracing per skill.
- Frontend: Next.js 15, React 19, streaming UI, accessibility-first (WCAG 2.2 AA, UDL principles).
- Distributed: NATS JetStream for events, Redis for session state, OpenTelemetry everywhere, p95 first-token < 800 ms on a 7B model (design target).
- Privacy: PII minimization at ingest, per-tenant encryption keys, xAPI statements to an LRS for interoperability.

**Core algorithms & pipelines.** Hybrid retrieval with reciprocal rank fusion; skill tracing (BKT baseline → DKT with attention); item generation constrained by Bloom level and skill node, validated by a judge model and by item-response statistics after use; spaced-repetition scheduling (FSRS).

**Milestones.** (1) Ingestion + hybrid retrieval + evaluation set (recall@k reported) — 3 weeks. (2) Tutor service with citations and structured outputs — 3 weeks. (3) Skill graph + BKT + assessment generator — 4 weeks. (4) NATS/Redis/OTel, load test, K8s manifests — 3 weeks. (5) Accessible UI, xAPI, facilitator analytics — 3 weeks.

**Live demo.** Public instance seeded with an open textbook chapter: pick a skill on the graph, ask a question, get a cited answer, take a generated 3-item check, watch the mastery estimate move — Pages front end + a small Fly/Render backend with a tiny model, rate-limited, no login.

### 2B. Certification-aligned projects (Oxford Saïd programmes on the Accredible wallet)

The wallet lists nine University of Oxford programmes (the profile mentions eleven; only nine are published on the wallet — worth reconciling). Each gets one purpose-built repo that turns the credential into demonstrable engineering. Proposed names are new, so no existing URL is affected.

| Programme (issued) | Proposed repo | Pitch | Stack | Demo |
|---|---|---|---|---|
| Artificial Intelligence (Jul 2023) | `ai-strategy-lab` | AI use-case triage tool: scores candidate initiatives on value, feasibility, risk (AI RMF), and produces a build/buy/wait recommendation with a portfolio view | Next.js + TypeScript, decision model as tested pure functions, export to PDF | Pages |
| Algorithmic Trading (Jan 2024) | `algo-trading-research-kit` | Backtesting engine with walk-forward validation, transaction-cost model and overfitting guards (deflated Sharpe); ties to fintech-risk-analytics | Python 3.12, polars, vectorbt-style engine, pytest, Streamlit | Streamlit + Pages report |
| Strategic Innovation (Feb 2024) | `innovation-portfolio-radar` | Three-horizons portfolio radar with option-value scoring and kill/scale gates | TypeScript, D3, tested scoring | Pages |
| Digital Marketing: Disruptive Strategy (Oct 2023) | `growth-analytics-engine` | Attribution + cohort analytics on synthetic event streams (privacy-safe): Markov-chain attribution, uplift, CAC/LTV | Python, DuckDB, Evidence or Streamlit | Streamlit |
| Entrepreneurship: Venture Finance (Oct 2023) | `venture-finance-modeler` | Cap-table, SAFE/convertible-note waterfall and Monte Carlo runway model with scenario comparison | TypeScript, tested finance math, spreadsheet import/export | Pages |
| Entrepreneurship: Venture Creation (Aug 2023) | `venture-canvas-studio` | Lean-canvas + hypothesis tracker with experiment scoring and evidence log (uses the Executive Shell) | TypeScript, localStorage/IndexedDB | Pages |
| Leading Professional Service Firms (Aug 2023) | `psf-utilization-analytics` | Utilization, leverage-ratio and pricing dashboard for consulting practices; directly supports the fall consulting launch | Python/FastAPI + Next.js, or Pages with CSV | Pages |
| Leading Strategic Projects (Aug 2023) | `strategic-project-radar` | Portfolio risk and earned-value dashboard with Monte Carlo schedule risk (reuses monte-carlo-simulator) | TypeScript, tested EVM math | Pages |
| Enterprise Leadership (May 2023) | `enterprise-operating-model-kit` | Operating-model diagnostic (capability heat-map, RACI generator, OKR cascade) with MkDocs playbook | TypeScript + MkDocs | Pages |

Recommended build order: `psf-utilization-analytics` and `ai-strategy-lab` first (they sell the consulting practice), then `algo-trading-research-kit` (deepest engineering), then the rest as T2 kit builds.

---

## SECTION 3: Executive Tone & Artifact Standard

The full machine-readable standard is `PORTFOLIO_STANDARD.md` (shipped in the kit). The essentials:

**README contract (every repo, same six headings).** Title with an executive tagline → badge row → 1 Executive Summary & Business Impact → 2 Demonstrated Competencies (Architecture & CS / Data Science & AI / Cybersecurity & Compliance / EdTech & Human-Centered Design) → 3 System Architecture & Data Flow (Mermaid) → 4 Technical Highlights & Engineering Decisions (ADR style: context → decision → consequence) → 5 Getting Started & Verification (one command) → 6 Live Demo & Production Showcase (URL, demo credentials, 30-second walkthrough).

**Badges, in this order, every repo.** CI/CD (`deploy.yml` workflow badge) · Coverage (measured %, Codecov once wired) · Security (`codeql.yml` badge) · License MIT · Live Demo. A badge that cannot be true yet is omitted, never faked.

**Evaluation metrics that must be real.** Test count and coverage % (from the CI run), lint/type-check status, security scan result (CodeQL / Bandit / Trivy / Checkov), Lighthouse performance + accessibility scores for any Pages demo, and for ML repos the evaluation metric on a named held-out set. Design targets are labelled as targets.

**CI/CD shape.** `.github/workflows/deploy.yml`: lint → test → security-scan → deploy (main only), pinned action versions, least-privilege `permissions:` per job. `.github/workflows/codeql.yml` weekly. Static demos deploy with `actions/deploy-pages` from the repo root so URLs never move.

**Diagrams.** Mermaid `flowchart LR`; trust boundaries as subgraphs titled "Trust Boundary: …"; four shared classDefs (client / service / data / security); security controls labelled on edges. One diagram per README minimum; sequence diagrams for auth flows.

**Executive Shell (all static demos).** Dark token set anchored on `#58A6FF` (already the profile's accent), Inter, sticky header with tagline + badges + "Take the 30-second tour", KPI strip computed from the demo's own data, footer with profile links. CSP meta + SRI on every CDN script; no inline handlers; WCAG AA; reduced-motion respected.

**Voice.** Calibrated claims ("parallels", "modelled on") over equivalence claims; problem → decision → consequence; numbers only when measured; "Freddrick Logan" as the author string; no tool fingerprints in metadata.

---

## 4. Rollout plan

| Batch | Repos | Effort | Outcome |
|---|---|---|---|
| 0 (this pass) | student-engagement-api, siem-log-analyzer, verifiable-academic-credentials, aws-terraform-gameday, kit | done | 4 flagships at principal grade; kit ready |
| 1 | neural-network-playground, epidemic-modeling-dashboard, cloud-architecture-designer, edtech-program-command-center | 1 pass | all 8 T1 flagships complete |
| 2 | 10 learning resources via `learning-resource-kit` | 1 pass | category IV uniform |
| 3 | 13 remaining T2 static demos via `_kit/static-demo` | 2 passes | category I–III uniform |
| 4 | Python/ML repos (DeepLearning-Charity, SentimentAnalysis-System, Crypto-Clustering, earthquake, cli tools) | 1–2 passes | packaging, tests, Streamlit demos |
| 5 | Consolidations + archive banners + profile README refresh (badges per project, tier labels) | 1 pass | no weak links left |
| 6 | Certification-aligned repos (2B), then Flagships 1–3 | ongoing | new signal |

**Applying a drop-in folder** (this session can read but not push to GitHub; each folder is a complete replacement tree):

```bash
git clone https://github.com/Freddricklogan/<repo>.git && cd <repo>
git checkout -b modernize
rsync -a --delete --exclude .git --exclude node_modules /path/to/drop-in/<repo>/ ./
git add -A && git commit -m "Modernize to portfolio standard v1"
git push -u origin modernize   # open a PR; CI runs on the PR
```

Then in repo Settings → Pages, set Source to "GitHub Actions" (one-time) so `deploy.yml` publishes to the unchanged URL.
