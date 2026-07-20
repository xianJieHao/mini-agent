
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

            messages = messages,

            tools = self.registry.get_all_schemas(),

            stream = False 

        )

        print(f"response:{response}")



# {
# 	'role': 'assistant',
# 	'content': '',
# 	'tool_calls': [{
# 		'id': 'call_o41z5dvo',
# 		'function': {
# 			'index': 0,
# 			'name': 'weather',
# 			'arguments': {
# 				'city': '广州'
# 			}
# 		}
# 	}]
# }




        if "tool_calls" not in response:
             return response["content"]


        #加入LLM回复
        messages.append(
            response
        )


        tool_calls = response.get("tool_calls")

        #获取工具调用信息


        for tool_call in tool_calls:
            
            function = tool_call["function"]

            tool_name = function["name"]

            args = function["arguments"]
            
           
            result = self.registry.execute(
                    tool_name,
                    **args
                    )
            
            messages.append(
                {
                    "role":"tool",
                    "content":result,
                    "tool_call_id":tool_call["id"]
                }
            )


        print(f"messages:{messages}")

        # 第二次调用LLM

        final_response = self.llm.chat(

            messages

        )


        return final_response["content"]
