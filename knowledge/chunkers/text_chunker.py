from knowledge.document import Document


class TextChunker:


    def __init__(
        self,
        chunk_size=500,
        overlap=100
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap


    def split(
        self,
        documents: list[Document]
    ) -> list[Document]:

        chunks = []


        for doc in documents:

            text = doc.page_content

            start = 0

            index = 1


            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]


                metadata = {
                    **doc.metadata,
                    "chunk": index
                }


                chunk = Document(
                    page_content=chunk_text,
                    metadata=metadata
                )


                chunks.append(chunk)


                index += 1

                start += self.chunk_size - self.overlap


        return chunks