from backend.llm import llm

def aggregator_agent(state):
    print("Entering aggregator")
    combined_summary = "\n".join(
        state["chunk_summaries"]
    )
    response = llm.invoke(
        f"""
        Create an executive summary from the following summaries.
        {combined_summary}
        """
    )
    state["final_summary"] = response.content
    state["logs"].append("Final Summary Generated")
    return state