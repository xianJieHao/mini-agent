from agent.message import MessageManager
from agent.executor import ToolExecutor



class Agent:


    def __init__(
        self,
        llm,
        registry
    ):

        self.llm = llm

        self.registry = registry

        self.executor = ToolExecutor(
            registry
        )



    def run(self,user_input):


        memory = MessageManager()


        memory.add_user(
            user_input
        )



        while True:


            response = self.llm.chat(

                messages=
                memory.get_messages(),

                tools=
                self.registry.get_all_schemas()

            )


            tool_calls = response.get(
                "tool_calls"
            )


            if not tool_calls:

                return response["content"]



            memory.add_assistant(
                response
            )



            for tool_call in tool_calls:


                result = self.executor.execute(
                    tool_call
                )


                memory.add_tool(

                    result["tool_call_id"],

                    result["content"]

                )