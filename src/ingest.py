from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter


def load_and_chunk_documents(
    data_dir: str,
    chunk_size: int = 400,
    chunk_overlap: int = 50
):
    """
    Loads RTI documents and splits them into legally safe chunks.
    """
    documents = SimpleDirectoryReader(
        input_dir=data_dir,
        recursive=True
    ).load_data()

    splitter = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    nodes = splitter.get_nodes_from_documents(documents)
    return nodes
