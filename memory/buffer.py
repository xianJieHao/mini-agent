class ConversationBuffer:


    def __init__(

        self,

        max_messages=4

    ):

        self.max_messages = max_messages



    def trim(

        self,

        messages

    ):


        if len(messages) <= self.max_messages:

            return messages


        return messages[-self.max_messages:]