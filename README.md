# 🤖 Frontdesk Engineering Test: Human-in-the-Loop AI Supervisor

A locally running system simulating a virtual AI receptionist. When the AI cannot answer a query, it escalates to a human supervisor via a help request UI. The supervisor responds, the AI replies back to the customer, and the knowledge base is automatically updated for future queries.

---

## 🛠️ Setup Instructions

### ✅ Requirements

* Python 3.8+
* pip (Python package manager)

### 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/saumya-jain20/frontdesk-human-in-the-loop.git
   cd HumanInTheLoop
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Supervisor Admin UI**

   ```bash
   python -m supervisor_ui.app
   ```

   Navigate to `http://127.0.0.1:5000` to:

   * View pending requests (Home)
   * View request history (`/history`)

5. **Run the AI Agent in another terminal**

   ```bash
   python -m agent.main_agent
   ```

---

## 🧠 Key Features

* **AI Agent Simulation**

  * CLI-based interface
  * Escalates unanswered queries

* **Knowledge Base**

  * `knowledge_base.json`
  * Case-insensitive question-answer store
  * Automatically updated when supervisor resolves queries

* **Request Lifecycle Management**

  * Status transitions:

    * `Pending` → `Resolved`
    * Or auto-marked as `Unresolved` after timeout
  * Timeout handled via async task with `threading.Timer`

* **Supervisor UI (Flask)**

  * View and respond to pending help requests
  * View complete history
  * Requests ordered by most recent

* **LiveKit Simulation**

  * Audio interactions mocked via CLI inputs
  * Placeholder logic for future voice/video escalation

* **Notifications (Mocked)**

  * Console logs simulate real-time alerts for escalation and follow-up

---

## 🔁 Request Lifecycle

1. **User Asks a Question**

   * If known → immediate AI response
   * If unknown → escalated to supervisor

2. **Pending Request is Created**

   * Shown on Supervisor UI
   * Timer starts (e.g., 3 minutes)

3. **If Supervisor Responds**

   * AI replies to customer
   * Request marked `Resolved`
   * Knowledge base is updated

4. **If Timeout Reached**

   * Request marked `Unresolved`
   * AI responds with fallback message

---


## 📚 System Design Notes

### 📂 File Structure

```
HumanInTheLoop/
├── agent/             # AI agent logic
├── request_store/     # Help request storage, status management
├── supervisor_ui/     # Flask-based UI
├── notifications/     # Simulated alerting system
├── knowledge_base.json
├── requests_db.json
├── requirements.txt
├── README.md
└── run.py
```

### 🧠 Knowledge Base

* JSON object with case-insensitive keys
* Updated automatically on every supervisor answer
* AI first checks this before escalating

### 🔄 Timeout Handling

* Timer starts when a new help request is created
* After defined time (default 3 mins), request marked `Unresolved`
* AI is notified and responds to user accordingly
* Uses `threading.Timer` for non-blocking behavior

---

## ⚙️ Scalability Plan

| Concern              | Current Handling            | Future Improvements                        |
| -------------------- | --------------------------- | ------------------------------------------ |
| Persistent storage   | JSON files                  | Migrate to SQLite/PostgreSQL               |
| Concurrency          | Thread-safe request updates | Switch to FastAPI + async I/O              |
| Multiple supervisors | Single shared queue         | Auth + assignment per supervisor           |
| Timeout handling     | Thread-based timer          | Background scheduler or job queue (Celery) |
| LiveKit integration  | CLI-based mock              | Real WebRTC integration with event hooks   |
| Real-time updates    | Page refresh/manual         | Add WebSockets for live UI updates         |

---

## 🧩 Modularity

* Clear separation of components:

  * `agent/` → CLI + AI logic
  * `request_store/` → Request lifecycle & storage
  * `supervisor_ui/` → Flask UI
  * `notifications/` → Console-based alerts
* All components communicate via service abstraction (function calls)

---

## 🧪 Improvements for Future

* Integrate real LiveKit API with audio streams
* Add authentication and session handling to UI
* Move to a persistent SQL-backed datastore
* Build dashboard with request metrics and filters
* Implement real-time push notifications (Twilio, WebSockets, etc.)
* Add escalation flow for unanswered/unresolved requests

---

## 🎥 Demo Video

*(Please include your recorded demo link here)*

---

## 📬 Submission Checklist

✅ Phase 1: Fully working simulation
✅ CLI-based AI agent and UI-based human supervisor
✅ Persistent knowledge base
✅ Escalation, resolution, and timeout flows
✅ Modular, clean code structure
✅ README with setup, architecture, and improvement ideas
✅ Ready for Phase 2 and production discussions

---
