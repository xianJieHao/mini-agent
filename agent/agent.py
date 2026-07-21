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
        self.memory = memory

        #为了防止循环卡死
        self._max_iterations = 3



    def run(self, user_input):

        

        self.memory.add(

            {
                "role":"user",

                "content":user_input

            }

        )


        iterations = 0
        
        while iterations < self._max_iterations:

            iterations += 1

            response = self.llm.chat(

                messages=self.memory.get(),

                tools=self.registry.get_all_schemas()

            )


            tool_calls = response.get(
                "tool_calls"
            )


            if not tool_calls:
                 #打印记忆
                self.memory.print()

                return response["content"]



            self.memory.add(response)



            for tool_call in tool_calls:


                result = self.executor.execute(
                    tool_call
                )


                
                self.memory.add(

                    {

                        "role":"tool",

                        "tool_call_id":result["tool_call_id"],

                        "content":result["content"]

                    }

                )

               
        
        # 超过最大迭代次数时返回最后响应
        return response.get("content", "达到最大迭代次数限制")