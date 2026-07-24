from knowledge.document import Document
from knowledge.stores.chroma_store import ChromaStore



docs=[

Document(
    page_content="员工一年有5天带薪年假",
    metadata={
        "source":"员工手册"
    }
),


Document(
    page_content="公司下午六点下班",
    metadata={
        "source":"考勤制度"
    }
)

]


store=ChromaStore()


store.add(
    docs
)


print("保存成功")