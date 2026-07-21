from agent.message import MessageManager
from agent.executor import ToolExecutor



class Agent:


    def __init__(
        self,
        llm,
        registry,
        memory
    ):

        self.llm = llm

        self.registry = registry

        self.executor = ToolExecutor(
            registry
        )
        self.memory = self.memory



    def run(self,user_input):


        self.memory.add(

            {
                "role":"user",

                "content":user_input

            }

        )


    


        while True:


            response = self.llm.chat(

                messages=self.memory.get(),

                tools=self.registry.get_all_schemas()

            )


            tool_calls = response.get(
                "tool_calls"
            )


            if not tool_calls:

                return response["content"]



            self.memory.add(response)



            for tool_call in tool_calls:


                result = self.executor.execute(
                    tool_call
                )


                
                self.messages.append(

                    {

                        "role":"tool",

                        "tool_call_id":tool_call["tool_call_id"],

                        "content":result["content"]

                    }

                )