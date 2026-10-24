# ApplyPilot AI — AI-Powered Resume Optimization & WhatsApp Job Application Agent

[![Tests](https://img.shields.io/badge/Tests-10%2F10%20Passed-emerald.svg)](tests/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%200.124-blue.svg)](https://fastapi.tiangolo.com)
[![WhatsApp Cloud API](https://img.shields.io/badge/WhatsApp-Cloud%20API%20v21.0-25D366.svg)](https://developers.facebook.com/)
[![License](https://img.shields.io/badge/License-Proprietary-slate.svg)]()

**ApplyPilot AI** is a production-oriented SaaS platform and AI agent that tailors resumes to job descriptions (JDs), calculates transparent, reproducible ATS match scores, generates ATS-optimized documents in 4 design styles (PDF and DOCX), and automates job application workflows through an official **WhatsApp Cloud API** integration and web dashboard.

---

## 🌟 Key Features

### 1. Master Resume Management (Feature A)
- Upload resumes in **PDF, DOCX, or TXT** formats.
- Extracts structured career data: contact info, work experience, titles, dates, education, skills, achievements, and quantified outcomes.
- Maintains a single source of truth (**Career Profile**) with verified facts.
- Ambiguity detection flags missing dates or unquantified bullets for user confirmation.
- **Strict Zero-Fabrication Rule**: Never invents employers, titles, tools, or dates.

### 2. Job Description Analyzer (Feature B)
- Accepts JDs via:
  - Direct text paste.
  - Live job posting URLs (with automated HTML extraction and anti-scraping fallback).
  - Document uploads.
  - WhatsApp messages (text, URLs, and attachments).
- Classifies seniority, mandatory skills, preferred skills, technical tools, responsibilities, and ATS keywords.

### 3. Transparent JD Match Scoring Engine (Feature D)
Calculates a reproducible score across **6 weighted dimensions** (totaling 100%):
- **Mandatory Skills**: 30%
- **Relevant Experience & Responsibilities**: 25%
- **Technical Tools & Domain Knowledge**: 15%
- **Required Qualifications & Certifications**: 10%
- **Relevant Achievements & Measurable Impact**: 10%
- **Preferred Skills & Additional Keywords**: 10%

Provides:
- **JD Match Score** (Before and After optimization).
- **Evidence Coverage**: % of explicit requirements supported by verified resume evidence.
- Full breakdown of matched mandatory skills, unverified requirements, and legitimate recommendations.
- **Zero Score Inflation**: No artificial score boosting or keyword repetition rewards.

### 4. AI Resume Tailoring Agent (Feature C & E)
- Rewrites bullet points using strong action verbs and role-specific terminology without changing underlying facts.
- Generates side-by-side diff with clear rationale for every modification.
- Downloads in **DOCX, PDF, and Plain Text** formats across 4 design styles:
  1. **ATS Classic**: Strict single-column, standard headings, maximum parser compatibility.
  2. **Modern Professional**: Clean navy blue accents and balanced typography.
  3. **Technical / Software Engineer**: Teal accents, prioritized technical competencies.
  4. **Product Manager / AI PM**: Bronze accents, emphasized cross-functional metrics.
- Built-in ATS compliance validator checks contact info, structure, and keyword density.

### 5. WhatsApp Cloud AI Agent & Live Simulator (Feature F)
- Official Meta WhatsApp Business Platform Cloud API integration with webhook verification (`hub.mode`, `hub.challenge`, `hub.verify_token`).
- Multi-turn state machine handles natural conversations:
  - Send resume ➔ receive confirmation.
  - Send JD link or text ➔ receive match report and tailored resume link.
  - Ask to view documents ➔ receive secure document link.
  - Approve submission ➔ verified submission confirmation.
- Opt-out (`STOP`, `UNSUBSCRIBE`) and Opt-in (`START`) consent handling.
- **Interactive Browser Emulator**: Test complete multi-turn WhatsApp flows directly in the Web UI without waiting for Meta account approval!

### 6. Job Application Automation & Tracker (Feature G & H)
- Prepares application packages including notice period, salary expectations, and work authorization answers.
- **Mandatory User Approval Gate**: Never submits applications without explicit candidate authorization.
- Duplicate submission prevention.
- Kanban & Table tracking dashboard with statuses: *Saved, Analyzing, Resume Ready, Awaiting Approval, Ready to Apply, Submitted, Under Review, Interview, Rejected, Offer*.
- CSV Export for all tracked applications.

### 7. AI Career Insights & Cross-JD Skill Gaps (Feature I)
- Aggregates market demand and recurring skill gaps across all analyzed job postings.
- Recommends prioritized learning paths and suggested portfolio projects without modifying the candidate's verified resume.

---

## 🏗️ System Architecture

```
ApplyPilot AI
├── app/
│   ├── main.py                  # FastAPI entry point, routes, static mount
│   ├── config.py                # Environment configuration & settings
│   ├── database.py              # SQLite / PostgreSQL engine & session
│   ├── models.py                # SQLAlchemy models (User, Resume, JD, App, WhatsApp)
│   ├── schemas.py               # Pydantic data schemas
│   ├── agents/
│   │   ├── llm_client.py        # LLM abstraction (OpenAI, Anthropic, or Deterministic)
│   │   ├── resume_parser.py     # Resume Parser Agent
│   │   ├── jd_analyzer.py       # JD Analyzer Agent (Text & URLs)
│   │   ├── matcher.py           # 6-Dimension Transparent Scoring Engine
│   │   ├── resume_tailor.py     # Zero-Fabrication Tailoring Agent
│   │   ├── ats_validator.py     # ATS Formatting & Keyword Density Validator
│   │   ├── application_assistant.py # Pre-screening & Approval Package
│   │   └── whatsapp_orchestrator.py # WhatsApp Cloud API State Machine
│   ├── services/
│   │   ├── document_service.py  # PDF/DOCX Parsing & 4-Template Generation
│   │   ├── job_submission.py    # Submission gate & verification
│   │   └── career_analytics.py  # Cross-JD skill gap aggregation
│   ├── routers/                 # REST API endpoints
│   ├── static/                  # CSS & interactive JavaScript controller
│   └── templates/               # SaaS dashboard HTML template
├── samples/                     # Synthetic test resumes & job descriptions
├── tests/                       # Automated pytest suite (10/10 passing)
├── run.py                       # Application launcher
└── requirements.txt
```

---

## ⚡ Quick Start

### 1. Prerequisites
- Python 3.8 or higher.
- Windows, macOS, or Linux.

### 2. Installation
```bash
# Clone or navigate to the directory
cd "c:\Users\Surajit Sadhu\Downloads\PM Projects"

# Install dependencies
python -m pip install -r requirements.txt
```

### 3. Run Automated Tests
```bash
python -m pytest tests/
```
Output:
```
tests/test_application_flow.py .                                         [ 10%]
tests/test_document_generator.py .                                       [ 20%]
tests/test_matcher.py ..                                                 [ 40%]
tests/test_parser.py ..                                                  [ 60%]
tests/test_tailor.py ..                                                  [ 80%]
tests/test_whatsapp_webhook.py ..                                        [100%]
============================= 10 passed in 2.35s ==============================
```

### 4. Launch the Application
```bash
python run.py
```
Open your browser at:
- **Web SaaS Dashboard**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive OpenAPI Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **WhatsApp Webhook Endpoint**: `http://127.0.0.1:8000/api/whatsapp/webhook`

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` to configure external credentials:

| Variable | Description | Default / Fallback |
|---|---|---|
| `DATABASE_URL` | SQLAlchemy database connection string | `sqlite:///./applypilot.db` |
| `SECRET_KEY` | Session and token secret key | Built-in secure key |
| `OPENAI_API_KEY` | OpenAI API key for GPT-4o-mini | Optional (uses Deterministic Engine if empty) |
| `ANTHROPIC_API_KEY` | Anthropic API key for Claude 3.5 Sonnet | Optional |
| `WHATSAPP_PHONE_NUMBER_ID` | Meta WhatsApp Cloud Phone Number ID | Optional (browser simulator works without it) |
| `WHATSAPP_ACCESS_TOKEN` | Meta System User permanent access token | Optional |
| `WHATSAPP_VERIFY_TOKEN` | Webhook verification handshake token | `applypilot_verify_token_secure_2026` |

---

## 🧪 Testing with Synthetic Data

Sample files are included in the `samples/` directory:
- `samples/sample_resume_swe.txt`: Lead Software Engineer resume.
- `samples/sample_resume_pm.txt`: Senior Product Manager resume.
- `samples/sample_jd_lead_engineer.txt`: Stripe Lead Backend Engineer JD.
- `samples/sample_jd_senior_pm.txt`: Datadog Senior Product Manager JD.

---

## 🛡️ Working Features vs External Credential Requirements

| Feature | Works Out-of-the-Box (Demo Mode) | Requires External Credentials |
|---|---|---|
| **Master Resume Upload & Parsing** | ✅ Yes (PyPDF, python-docx, heuristic engine) | None |
| **Career Profile Editor & Storage** | ✅ Yes (SQLite / SQLAlchemy) | Optional PostgreSQL |
| **JD Text Input & Requirement Extraction** | ✅ Yes (Deterministic parsing & ATS scoring) | Optional OpenAI/Anthropic API Key |
| **Public URL Parsing** | ✅ Yes (BeautifulSoup4 safe scraper) | None |
| **6-Dimension Match Scoring Engine** | ✅ Yes (Full reproducible mathematical engine) | None |
| **Factual Zero-Fabrication Tailoring** | ✅ Yes (Action verb & alignment engine) | Optional OpenAI/Anthropic API Key |
| **DOCX and PDF Generation (4 styles)** | ✅ Yes (ReportLab & python-docx) | None |
| **Interactive WhatsApp Live Simulator** | ✅ Yes (Full in-browser chat emulator) | None |
| **Official WhatsApp Cloud API Delivery** | Interface ready with webhook verification | Meta WhatsApp Cloud API credentials |
| **Application Tracker & CSV Export** | ✅ Yes | None |
| **Career Skill-Gap Analytics** | ✅ Yes | None |
