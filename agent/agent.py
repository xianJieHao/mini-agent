
from agent.registry import ToolRegistry
from llm.ollama_client import OllamaClient
from tools.weather import WeatherTool
from tools.sales import SalesTool



class Agent:


    def __init__(self,llm,registry):

        self.llm = llm
        self.registry = registry
  
    
    def run(self, message):

        messages = [

            {
                "role":"user",
                "content":message
            }

        ]

        #第一次请求LLM，获取tool调用信息
        response = self.llm.chat(

            messages,

            self.registry.get_all_schemas()

        )


        if "tool_calls" not in response:
             return response["content"]


        tool_calls = response.get("tool_calls")

        #获取工具调用信息
        tool_call = tool_calls[0]

        function = tool_call["function"]

        tool_name = function["name"]

        args = function["arguments"]
        
        result = self.registry.execute(
            tool_name,
            **args
        )
        #加入LLM回复

        messages.append(
            response
        )

        #加入工具结果
        messages.append(

            {

                "role": "tool",

                "content": result,

                "tool_call_id": tool_call["id"]

            }
        )


        # 第二次调用LLM

        final_response = self.llm.chat(

            messages

        )


        return final_response["content"]
