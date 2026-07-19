from llm.ollama_client import OllamaClient

client = OllamaClient()

messages = [
    {
        "role": "user",
        "content": "广州今天的天气怎么样？"
    }
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "weather",
            "description": "查询天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

response = client.chat(
    messages=messages,
    tools=tools
)


print(response)