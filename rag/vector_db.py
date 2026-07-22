import math


class MiniVectorDB:


    def __init__(self) -> None:

        self.documents = []



    def add(

        self,

        embedding,

        document

    ) -> None:

        self.documents.append(

            {

                "embedding":embedding,

                "document":document

            }

        )



    def distance(

        self,

        a,

        b

    ) -> float:

        total = 0


        for i in range(len(a)):

            total += (a[i]-b[i])**2


        return math.sqrt(total)



    def search(

        self,

        query_embedding

    ):


        results = []


        for item in self.documents:


            score: float = self.distance(

                query_embedding,

                item["embedding"]

            )


            results.append(

                {

                    "score":score,

                    "document":item["document"]

                }

            )


        results.sort(

            key=lambda x:x["score"]

        )


        return results
    