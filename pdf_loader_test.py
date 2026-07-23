
from knowledge.loaders.pdf_loader import PDFLoader 


class PdfLoaderTest:

    def test(self):
       pdf = PDFLoader()
       data = pdf.load(path="/Users/jiehao/Downloads/公司员工手册.pdf")
       return data



if __name__ == "__main__":
     d = PdfLoaderTest()
     print(d.test())