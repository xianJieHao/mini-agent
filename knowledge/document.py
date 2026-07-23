from dataclasses import dataclass, field

@dataclass
class Document:

    page_content: str

    metadata: dict = field(default_factory=dict)

    def __repr__(self):
        return f"Document(content={self.page_content[:20]}, metadata={self.metadata})"