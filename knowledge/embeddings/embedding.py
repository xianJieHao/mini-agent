from abc import ABC, abstractmethod


class Embedding(ABC):


    @abstractmethod
    def embed(
        self,
        texts:list[str]
    ) -> list[list[float]]:

        pass