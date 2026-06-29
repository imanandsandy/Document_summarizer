from backend.graph.workflow import graph

result = graph.invoke(
    {
        "pdf_path": r"C:\Users\sande\PycharmProjects\tcs_ps\sandeep_resume.pdf",
        "document_text": "",
        "chunks": [],
        "chunk_summaries": [],
        "final_summary": "",
        "quality_score": 0,
        "logs": []
    }
)

print("\nSUMMARY:\n")
print(result["final_summary"])

print("\nQUALITY SCORE:")
print(result["quality_score"])

print("\nLOGS:")
for log in result["logs"]:
    print(log)