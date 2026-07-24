import chromadb


class ChromaStore:


    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma"
        )


        self.collection = self.client.get_or_create_collection(
            name="knowledge"
        )



    def add(
        self,
        documents
    ):

        ids=[]
        texts=[]
        metadatas=[]


        for index,doc in enumerate(documents):

            ids.append(
                str(index)
            )

            texts.append(
                doc.page_content
            )

            metadatas.append(
                doc.metadata
            )


        self.collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas
        )