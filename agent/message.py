class MessageManager:


    def __init__(self):

        self.messages = []



    def add_user(self, content):

        self.messages.append(

            {
                "role":"user",
                "content":content
            }

        )



    def add_assistant(self,message):

        self.messages.append(message)



    def add_tool(
        self,
        tool_call_id,
        content
    ):

        self.messages.append(

            {

                "role":"tool",

                "tool_call_id":
                    tool_call_id,

                "content":
                    content

            }

        )



    def get_messages(self):

        return self.messages