import json
from config import KNOWLEDGE_BASE_PATH

def load_knowledge_base():
    try:
        with open(KNOWLEDGE_BASE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_knowledge_base(kb):
    with open(KNOWLEDGE_BASE_PATH, 'w') as f:
        json.dump(kb, f, indent=4)

def get_answer(question):
    kb = load_knowledge_base()
    return kb.get(question.lower())

def learn_answer(question, answer):
    kb = load_knowledge_base()
    kb[question.lower()] = answer
    save_knowledge_base(kb)
