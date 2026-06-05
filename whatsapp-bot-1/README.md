# [Project Name] — WhatsApp Chatbot

> **Client:** [Anonymized — e.g. "Real Estate Client, Raipur"]  
> **Built by:** Rohit/Devansh  
> **Mentor:** Kapil & Apratim  
> **Timeline:** Week X – Week Y  
> **Status:** 🔵 In Progress / ✅ Delivered

---

## Problem Statement

*1–2 sentences: What was the client's problem? What were they doing manually that this bot replaces?*

Example: "Client was handling 50+ daily WhatsApp inquiries manually. Response time was 3–4 hours. Lead data was being lost."

---

## Solution Overview

*What does this bot do? List the core flows.*

- Greets new users and qualifies them (name, requirement, budget)
- Captures lead data to a Google Sheet / database
- Sends confirmation message + follow-up after 24 hrs
- Escalates to human agent on keyword trigger ("speak to agent")

---

## Architecture

```
User (WhatsApp)
    ↓
Meta WhatsApp Business API
    ↓
Webhook → Flask App (this repo)
    ↓
[Business Logic Layer]
    ↓
Database (SQLite/PostgreSQL) + [Optional: Google Sheets / CRM]
```

*(Add a proper diagram in `../docs/architecture/bot-1-architecture.png` and link it here)*

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Framework | Flask |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Hosting | [e.g. Railway / DigitalOcean / VPS] |
| Webhook Tunnel (dev) | Ngrok |
| WhatsApp API | Meta Cloud API |

---

## Local Setup

### Prerequisites
- Python 3.10+
- Ngrok account (free tier works)
- Meta Developer account with WhatsApp Business API access

### Steps

```bash
# 1. Navigate to this project
cd whatsapp-bot-1

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Fill in actual values in .env (get credentials mentors if required)

# 5. Run the app
python app.py

# 6. In a new terminal — expose localhost via ngrok
ngrok http 5000

# 7. Copy the ngrok URL and set it as your webhook in Meta Developer Console
# Webhook URL: https://your-ngrok-url.ngrok.io/webhook
# Verify Token: (use the value from your .env)
```

---

## Environment Variables

See `.env.example` for all required variables. Never commit `.env`.

```
WHATSAPP_TOKEN=          # Meta API access token
VERIFY_TOKEN=            # Your custom webhook verify token
PHONE_NUMBER_ID=         # WhatsApp Business phone number ID
DATABASE_URL=            # SQLite path or PostgreSQL connection string
```

---

## Project Structure

```
whatsapp-bot-1/
│
├── app.py                  # Flask app entry point + webhook handler
├── requirements.txt        # Pinned dependencies
├── .env.example            # Environment variable template
│
├── handlers/
│   ├── message_handler.py  # Routes incoming messages to correct flow
│   ├── lead_flow.py        # Lead capture conversation logic
│   └── escalation.py       # Human handoff logic
│
├── models/
│   └── lead.py             # Database model for leads
│
├── utils/
│   ├── whatsapp_api.py     # WhatsApp API wrapper (send message, etc.)
│   └── db.py               # Database connection helpers
│
├── tests/
│   ├── test_webhook.py     # Webhook verification tests
│   └── test_flows.py       # Conversation flow unit tests
│
└── docs/
    └── conversation-flow.md  # Decision tree / flow diagram
```

---

## Deployment

### Staging
```bash
# [Document your staging server steps here]
# e.g. push to Railway, or SSH to VPS
```

### Production
```bash
# [Document production deployment steps here]
# Include: server, process manager (gunicorn/systemd), reverse proxy (nginx)
```

**Checklist before going live:**
- [ ] All tests passing (`pytest`)
- [ ] `.env` set on server (not committed)
- [ ] Webhook URL updated in Meta Console to production URL
- [ ] Database backed up
- [ ] Client tested on staging and approved
- [ ] Gunicorn running (not Flask dev server)

---

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=term-missing
```

---

## Known Issues / Limitations

*(Document honestly — this helps future interns)*

- [ ] Issue 1
- [ ] Issue 2

---

## Lessons Learned

*(Fill this out at project end — it becomes part of your case study)*

- What was harder than expected?
- What would you do differently?
- What pattern will you reuse in Bot #2?

---

## Links

- 📄 Case Study: `../docs/case-studies/bot-1-case-study.md`
- 🏗️ Architecture Diagram: `../docs/architecture/bot-1-architecture.png`
- 📝 Blog Post: [Link to published post]
- 🔗 LinkedIn Post: [Link]
