from llm.ollama_client import OllamaClient
from agent.planner import Planner
from agent.registry import ToolRegistry
from tools.weather import WeatherTool
from tools.sales import SalesTool
from agent.agent import Agent


def main():

    client = OllamaClient()

    planner = Planner()

    registry = ToolRegistry()

    registry.register(WeatherTool())

    registry.register(SalesTool())


    agent = Agent(client, planner, registry)

    while True:

        question = input("你：")

        if question == "exit":
            break

        answer = agent.chat(question)

        print(answer)


if __name__ == "__main__":

    main()