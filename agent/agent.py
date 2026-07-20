from llm.ollama_client import OllamaClient
from agent.registry import ToolRegistry
import json


class Agent:


    def __init__(self,llm,registry):

        self.llm = llm
        self.registry = registry



    def run(self,message):

        messages = [

            {
                "role":"user",
                "content":message
            }

        ]


        while True:


            response = self.llm.chat(

                messages=messages,

                tools=self.registry.get_all_schemas()

            )


            print("LLM Response:")
            print(response)



            # 没有工具调用
            if "tool_calls" not in response:

                return response["content"]



            # 保存assistant消息

            messages.append(response)



            tool_calls = response["tool_calls"]



            for tool_call in tool_calls:


                function = tool_call["function"]


                tool_name = function["name"]


                args = function["arguments"]



                print(
                    f"执行工具:{tool_name}"
                )



                result = self.registry.execute(

                    tool_name,

                    **args

                )



                messages.append(

                    {

                        "role":"tool",

                        "tool_call_id":
                            tool_call["id"],

                        "content":
                            json.dumps(
                                result,
                                ensure_ascii=False
                            )

                    }

                )