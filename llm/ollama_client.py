# llm/ollama_client.py

import requests


class OllamaClient:

    def __init__(
        self,
        base_url="http://localhost:11434",
        model="deepseek-r1:latest"
    ):
        self.base_url = base_url
        self.model = model


    def chat(self, message):

        url = f"{self.base_url}/api/chat"


        data = {
            "model": self.model,

            "messages":[
                {
                    "role":"user",
                    "content":message
                }
            ],

            "stream":False
        }


        response = requests.post(
            url,
            json=data
        )


        result = response.json()


        return result["message"]["content"]