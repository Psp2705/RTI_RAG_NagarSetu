from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.retrievers import VectorIndexRetriever


class RTIRetriever:
    def __init__(self, nodes, top_k: int = 3):
        self.embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

        self.index = VectorStoreIndex(
            nodes,
            embed_model=self.embed_model
        )

        self.retriever = VectorIndexRetriever(
            index=self.index,
            similarity_top_k=top_k
        )

    def retrieve(self, query: str):
        return self.retriever.retrieve(query)
