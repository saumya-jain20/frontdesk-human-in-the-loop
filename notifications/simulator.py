def notify_supervisor(question):
    print(f"[SUPERVISOR ALERT] Help needed: '{question}'")

def notify_customer(customer_id, message):
    print(f"[TEXT TO {customer_id}]: {message}")
