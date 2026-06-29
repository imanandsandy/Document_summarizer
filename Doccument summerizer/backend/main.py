from fastapi import FastAPI, UploadFile, File
from backend.graph.workflow import graph
import os

app = FastAPI()
os.makedirs("uploads", exist_ok=True)
@app.get("/")
def home():
    return {
        "message": "Agentic Document Summarizer Running"
    }
@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    initial_state = {
        "pdf_path": file_path,
        "document_text": "",
        "chunks": [],
        "chunk_summaries": [],
        "final_summary": "",
        "quality_score": 0,
        "logs": []
    }

    result = graph.invoke(initial_state)
    return {
        "summary": result["final_summary"],
        "quality_score": result["quality_score"],
        "logs": result["logs"]
    }