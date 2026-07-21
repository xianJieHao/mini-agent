
from agent.agent import Agent
from agent.registry import ToolRegistry
from llm.ollama_client import OllamaClient
from tools.sales import SalesTool
from tools.weather import WeatherTool
from memory.memory import Menmory



def main():


    llm = OllamaClient()
    registry = ToolRegistry()
    registry.register(WeatherTool())
    registry.register(SalesTool())
    memory = Menmory()
    agent = Agent(llm=llm, registry=registry, memory=memory)

    while True:

        user_input = input(
            "You:"
        )


        if user_input == "exit":
            break


        answer = agent.run(
            user_input
        )


        print(
            "AI:",
            answer
        )



if __name__ == "__main__":

    main()