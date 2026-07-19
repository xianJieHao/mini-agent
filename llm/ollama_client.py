import requests


class OllamaClient:

    def __init__(self):

        self.base_url = "http://localhost:11434"

        self.model = "qwen3-coder:30b"

    def chat(
        self,
        messages,
        tools=None,
        stream=False,
    ):

        url = f"{self.base_url}/api/chat"

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
        }

        if tools is not None:
            payload["tools"] = tools

        response = requests.post(
            url,
            json=payload,
        )

        response.raise_for_status()

        return response.json()["message"]