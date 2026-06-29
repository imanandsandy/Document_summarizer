from backend.llm import llm
def summarizer_agent(state):
    print("Entering Summarizer")
    summaries = []
    total_chunks = len(state["chunks"])

    for i, chunk in enumerate(state["chunks"][:5]):
        print(f"Summarizing chunk {i + 1}/5")

        response = llm.invoke(
            f"""
            Summarize the following content in concise bullet points.

            {chunk}
            """
        )
        summaries.append(response.content)

    print("Exiting Summarizer")
    state["chunk_summaries"] = summaries
    state["logs"].append(
        "Chunk Summaries Generated"
    )
    return state