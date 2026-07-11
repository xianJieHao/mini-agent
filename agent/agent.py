
from agent.planner import Planner
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
        self.planner = Planner()

    def chat(self, message):

        action = self.planner.plan(
            message
        )
      
        print(
            "Planner:",
            action
        )

        if action["action"] == "chat":
            return self.llm.chat(message)
        
        tool = self.registry.get(action["action"])

        result = tool.execute(
            **action["params"]
        )

        return result