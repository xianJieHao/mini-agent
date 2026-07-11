from abc import ABC, abstractmethod

class Tool(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass

    @property
    @abstractmethod
    def parameters(self):
        """
        告诉LLM这个工具需要哪些参数
        """
        pass