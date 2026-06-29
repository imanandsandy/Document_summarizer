from langgraph.graph import StateGraph, END
from backend.state import SummaryState
from backend.agents.ingestion import ingestion_agent
from backend.agents.chunking import chunking_agent
from backend.agents.summarizer import summarizer_agent
from backend.agents.aggregator import aggregator_agent
from backend.agents.evaluator import evaluator_agent
from backend.agents.refiner import refiner_agent
def route(state):
    if state["quality_score"] < 8:
        return "refine"
    return "end"
workflow = StateGraph(SummaryState)


workflow.add_node("ingest", ingestion_agent)
workflow.add_node("chunk", chunking_agent)
workflow.add_node("summarize", summarizer_agent)
workflow.add_node("aggregate", aggregator_agent)
workflow.add_node("evaluate", evaluator_agent)
workflow.add_node("refine", refiner_agent)

workflow.set_entry_point("ingest")

workflow.add_edge("ingest", "chunk")
workflow.add_edge("chunk", "summarize")
workflow.add_edge("summarize", "aggregate")
workflow.add_edge("aggregate", "evaluate")

workflow.add_conditional_edges(
    "evaluate",
    route,
    {
        "refine": "refine",
        "end": END
    }
)

workflow.add_edge("refine", END)
graph = workflow.compile()