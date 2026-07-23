import os

from pypdf import PdfReader

from knowledge.document import Document
from knowledge.loaders.loader import Loader

class PDFLoader(Loader):

    def load(self, path:str):

        reader = PdfReader(path)

        documents = []
        for page_number, page in enumerate(reader.pages):
            text = page.extract_text() or ""

            if not text.strip():
                continue

            filename = os.path.basename(path)

            doc = Document(
                page_content=text,
                metadata={
                    "source": filename,
                    "page": page_number + 1
                }
            )
            documents.append(doc)

        return documents

