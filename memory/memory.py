from memory.buffer import ConversationBuffer


class Menmory:
    def __init__(

        self,

        max_messages=20

    ):


        self.messages = []


        self.buffer = ConversationBuffer(

            max_messages

        )

    def add(self,message):
        self.messages.append(message)

    def get(self):
        return self.buffer.trim(self.messages)
    
    def clear(self):
        self.messages = []

    def print(self):
        """打印内存中的消息"""
        print("\n" + "="*50)
        print("📋 Conversation Memory")
        print("="*50)
        
        if not self.messages:
            print("  (No messages)")
        else:
            print(f"  Total Messages: {len(self.messages)}")
            print(f"  Max Messages: {self.buffer.max_messages}")
            print("-"*50)
            
            # Print all messages
            for i, msg in enumerate(self.messages, 1):
                print(f"\n  [{i}] {msg}")
        
        print("="*50 + "\n")

