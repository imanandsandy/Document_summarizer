from backend.llm import llm
import re
def evaluator_agent(state):
    response = llm.invoke(
        f"""
        Rate this summary from 1 to 10.
        Return ONLY the number.
        Summary:
        {state['final_summary']}
        """
    )
    match = re.search(r"\d+", response.content)
    score = int(match.group()) if match else 7
    state["quality_score"] = score
    state["logs"].append(
        f"Quality Score = {score}"
    )
    return state