from abc import ABC,abstractmethod

from knowledge.document import Document


class Loader(ABC):

    @abstractmethod
    def load(self,path:str)->list[Document]:
        print("加载文件")