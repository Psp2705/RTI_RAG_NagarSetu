from src.ingest import load_and_chunk_documents
from src.retriever import RTIRetriever
from src.templates import RTI_TEMPLATE


def build_questions_from_context(nodes):
    questions = []
    for i, node in enumerate(nodes, start=1):
        line = node.text.strip().split(".")[0]
        questions.append(f"{i}. {line}")
    return "\n".join(questions)


class RTIRAGPipeline:
    def __init__(self, data_dir: str):
        nodes = load_and_chunk_documents(data_dir)
        self.retriever = RTIRetriever(nodes)

    def generate_rti(
        self,
        user_query: str,
        authority: str,
        applicant_name: str
    ) -> str:
        retrieved_nodes = self.retriever.retrieve(user_query)

        if not retrieved_nodes:
            return "❌ No legal basis found. RTI draft cannot be generated."

        questions = build_questions_from_context(retrieved_nodes)

        return RTI_TEMPLATE.format(
            authority=authority,
            questions=questions,
            applicant_name=applicant_name
        )
