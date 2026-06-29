from backend.llm import llm
def refiner_agent(state):
    response = llm.invoke(
        f"""
        Improve this summary.
        Make it concise, clear and professional.
        {state['final_summary']}
        """
    )
    state["final_summary"] = response.content
    state["logs"].append("Summary Refined")
    return state