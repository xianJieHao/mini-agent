from knowledge.document import Document


class TextChunker:
    def __init__(self,chunker_size=500,overlap=100):
        self.chunker_size = chunker_size
        self.overlap = overlap

    def split(self, documents:list[Document])->list[Document]:

        pass 