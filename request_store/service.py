import json
import os
from config import DB_PATH
from request_store.models import HelpRequest
from agent.knowledge_base import learn_answer
from notifications.simulator import notify_customer
from datetime import datetime, timedelta

TIMEOUT_MINUTES = 5

def _load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def _save_db(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def create_request(customer_id, question):
    req = HelpRequest(customer_id, question)
    db = _load_db()
    db.append(req.to_dict())
    _save_db(db)

def get_pending_requests():
    return [r for r in _load_db() if r['status'] == 'Pending']

def get_all_requests():
    return _load_db()

def update_request(request_id, answer):
    db = _load_db()
    for r in db:
        if r['id'] == request_id:
            r['status'] = 'Resolved'
            r['answer'] = answer
            learn_answer(r['question'], answer)
            notify_customer(r['customer_id'], answer)
    _save_db(db)

def mark_unresolved_requests():
    """Mark all pending requests older than TIMEOUT_MINUTES as Unresolved."""
    db = _load_db()
    now = datetime.utcnow()
    updated = False

    for r in db:
        if r['status'] == 'Pending':
            req_time = datetime.fromisoformat(r['timestamp'])
            if now - req_time > timedelta(minutes=TIMEOUT_MINUTES):
                r['status'] = 'Unresolved'
                updated = True

    if updated:
        _save_db(db)