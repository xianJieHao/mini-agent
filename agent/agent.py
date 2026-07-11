
from agent.registry import ToolRegistry
from llm.ollama_client import OllamaClient
from tools.weather import WeatherTool
from tools.sales import SalesTool



class Agent:


    def __init__(self):

        self.llm = OllamaClient()
        self.registry = ToolRegistry()
        self.registry.register(WeatherTool())
        self.registry.register(SalesTool())


    def chat(self, message):

        tools = self.registry.list_tools()

        print("当前可用工具:")

        for tool in tools:

            print(
                tool.name,
                ":",
                tool.description
            )

        answer = self.llm.chat(
            message
        )

        return answer