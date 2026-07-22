from llm.ollama_client import OllamaClient
from rag.vector_db import MiniVectorDB
import ollama

# client = OllamaClient()

# messages = [
#     {
#         "role": "user",
#         "content": "广州今天的天气怎么样？"
#     }
# ]

# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "weather",
#             "description": "查询天气",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "city": {
#                         "type": "string",
#                         "description": "城市名称"
#                     }
#                 },
#                 "required": ["city"]
#             }
#         }
#     }
# ]

# response = client.chat(
#     messages=messages,
#     tools=tools
# )


# print(response)

db = MiniVectorDB()

db.add(

    [0.1,0.2],

    "广州"

)

db.add(

    [0.8,0.9],

    "北京"

)

db.add(

    [0.15,0.25],

    "深圳"

)

result = db.search(

    [0.11,0.21]

)
# print(result)



response = ollama.embed(

    model="nomic-embed-text",

    input="广州天气很好"

)

print(response["embeddings"][0][:10])