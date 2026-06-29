from typing import TypedDict, List

class SummaryState(TypedDict):
    pdf_path: str
    document_text: str
    chunks: List[str]
    chunk_summaries: List[str]
    final_summary: str
    quality_score: int
    logs: List[str]