
from agent.agent import Agent
from agent.registry import ToolRegistry
from llm.ollama_client import OllamaClient
from tools.sales import SalesTool
from tools.weather import WeatherTool



def main():


    llm = OllamaClient()
    registry = ToolRegistry()
    registry.register(WeatherTool())
    registry.register(SalesTool())
    
    agent = Agent(llm, registry)

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