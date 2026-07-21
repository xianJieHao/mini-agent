class Menmory:
    def __init__(self):
        self.messages = []

    def add(self,message):
        self.messages.append(message)

    def get(self):
        return self.messages
    
    def clear(self):
        self.messages = []

