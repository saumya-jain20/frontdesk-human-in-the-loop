import uuid
from datetime import datetime

class HelpRequest:
    def __init__(self, customer_id, question, status='Pending', answer=None):
        self.id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.question = question
        self.status = status
        self.answer = answer
        self.timestamp = datetime.utcnow().isoformat()
    
    def to_dict(self):
        return self.__dict__
