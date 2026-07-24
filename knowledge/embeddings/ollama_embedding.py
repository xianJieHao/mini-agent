import requests


class OllamaEmbedding:


    def __init__(
        self,
        model="nomic-embed-text",
        url="http://localhost:11434/api/embeddings"
    ):

        self.model = model
        self.url = url



    def embed(
        self,
        texts:list[str]
    ):

        vectors=[]


        for text in texts:

            response = requests.post(
                self.url,
                json={
                    "model":self.model,
                    "prompt":text
                },
                timeout=30
            )

            response.raise_for_status() 

            data=response.json()


            vectors.append(
                data["embedding"]
            )


        return vectors