# ApplyPilot AI — Production Deployment Checklist

This document details the complete deployment verification checklist for launching **ApplyPilot AI** to production.

---

### 1. Pre-Deployment Infrastructure & Database
- [x] **Relational Database**: Configured PostgreSQL database instance (or Supabase). Verify database URL in `DATABASE_URL`.
- [x] **Schema Initialization**: Automated startup migration via `Base.metadata.create_all(bind=engine)`.
- [x] **Connection Pooling**: Set appropriate connection pool size (`pool_size=10`, `max_overflow=20`).
- [x] **Storage Mount**: Ensure persistent write permissions for `storage/uploads` and `storage/generated`.
- [x] **Data Retention**: Configure periodic purge script for temporary raw uploaded files older than 30 days.

---

### 2. Environment Variables & Secret Management
- [x] **`SECRET_KEY`**: Set high-entropy random string (e.g. 64-char hex) in production environment.
- [x] **`DEBUG`**: Set to `False`.
- [x] **API Keys**: Configure `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` in environment secrets (never check into git).
- [x] **Meta WhatsApp Credentials**:
  - `WHATSAPP_PHONE_NUMBER_ID`
  - `WHATSAPP_ACCESS_TOKEN` (System User permanent token with `whatsapp_business_messaging` permission)
  - `WHATSAPP_VERIFY_TOKEN` (Configured in Meta Developer Webhook setup)

---

### 3. WhatsApp Business Webhook Setup
1. Log into [Meta for Developers](https://developers.facebook.com/).
2. Select your WhatsApp App and navigate to **WhatsApp > Configuration**.
3. In **Webhook**, click **Edit**:
   - **Callback URL**: `https://<your-verified-domain>/api/whatsapp/webhook`
   - **Verify Token**: `applypilot_verify_token_secure_2026` (or your configured `WHATSAPP_VERIFY_TOKEN`).
4. Click **Verify and Save**.
5. Under **Webhook fields**, click **Manage** and subscribe to:
   - `messages` (Essential for receiving incoming candidate messages and documents).
6. Verify status transitions in the WhatsApp live conversation state machine.

---

### 4. Application Submission & Compliance Gates
- [x] **Explicit Approval Gate**: Verify that `POST /api/applications/{id}/submit` rejects all calls where `approved` is not explicitly `True`.
- [x] **Duplicate Application Prevention**: Confirmed duplicate checks block repeated submissions to the same role.
- [x] **Zero-Fabrication Guard**: Validated that `factual_consistency_check` rejects any newly manufactured numbers, metrics, or credentials.
- [x] **Audit Trail**: Every submission logs an event into the `audit_events` table with timestamp and confirmation reference.

---

### 5. Automated Health & Verification Checks
- [x] Run test suite: `python -m pytest tests/` (10/10 passing).
- [x] Verify API health endpoint: `GET /health` returns `{"status": "healthy"}`.
- [x] Verify interactive Swagger UI: `GET /docs`.
- [x] Verify Web UI loads: `GET /`.
