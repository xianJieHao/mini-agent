class TextChunker:

    def __init__(

        self,

        chunk_size=500,

        overlap=100

    ):

        if overlap >= chunk_size:

            raise ValueError(

                "overlap 必须小于 chunk_size"

            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text):

        if not text:
            return []

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks

if __name__ == "__main__":
    # 构造测试文本
    test_text = """人工智能（AI）是一门旨在使机器模拟人类智能的技术科学。
它包含机器学习、深度学习、自然语言处理、计算机视觉等多个方向。
大语言模型属于自然语言处理分支，可以理解人类语言、生成通顺文本。
文本分块（chunk）常用于知识库、RAG检索场景，把长文本切割成小段。"""

    # 实例化，调小参数方便观察效果
    chunker = TextChunker(chunk_size=30, overlap=10)
    chunks = chunker.split(test_text)

    # 打印结果
    print(f"一共分割出 {len(chunks)} 个片段：")
    for idx, seg in enumerate(chunks):
        print(f"\n【片段{idx+1}】")
        print(repr(seg))