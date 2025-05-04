from agent.livekit_handler import handle_incoming_call

def start_simulation():
    while True:
        customer_id = input("\nEnter customer ID (or 'exit'): ")
        if customer_id.lower() == 'exit':
            break
        question = input("Customer's question: ")
        handle_incoming_call(customer_id, question)

if __name__ == "__main__":
    start_simulation()
