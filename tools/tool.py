from abc import ABC, abstractmethod


class Tool(ABC):

    @property
    @abstractmethod
    def schema(self):
        """
        返回 Tool Schema
        """
        pass


    @abstractmethod
    def execute(self, **kwargs):
        pass