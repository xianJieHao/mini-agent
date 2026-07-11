import json
import config.config 
import requests


class OllamaClient:
    def __init__(self):
        self.host = config.config.Config().host 
        self.model = config.config.Config().model

    def chat(self, message):
        url = f"{self.host}/api/chat"
        print(f"当前模型: {self.model}")
        print(f"请求信息: {message}")
        data = {
            "model": self.model,
            "messages": message,
            "stream": True,
        }

        response = requests.post(
            url,
            json=data,
            stream=True
        )
        anwer = ""
      
        for line in response.iter_lines():
            if line:
                
                chunk = json.loads(line)
             
                text = chunk["message"]["content"]
                anwer += text
                print(
                    text,
                    end="",
                    flush=True
                )
        print()
        return anwer