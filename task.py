class Task:
    def __init__(self, text):
        self.text = text
        self.done = False
        
    def toggle(self):
        self.done = not self.done
    
    def to_dict(self):
        return {
            "text": self.text,
            "done": self.done
        }
    
    @staticmethod
    def from_dict(data):
        t = Task(data["text"])
        t.done = data["done"]
        return t