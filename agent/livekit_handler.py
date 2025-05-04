from agent.knowledge_base import get_answer
from request_store.service import create_request
from notifications.simulator import notify_supervisor, notify_customer

def handle_incoming_call(customer_id, question):
    print(f"\n[Incoming Call] Customer {customer_id}: {question}")
    answer = get_answer(question)
    if answer:
        notify_customer(customer_id, answer)
    else:
        notify_customer(customer_id, "Let me check with my supervisor and get back to you.")
        create_request(customer_id, question)
        notify_supervisor(question)

def receive_call():
    print("Simulating incoming call...")
    question = input("Customer: ")
    return question