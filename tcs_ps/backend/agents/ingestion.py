from pypdf import PdfReader
def ingestion_agent(state):
    print("Reading:", state["pdf_path"])
    reader = PdfReader(state["pdf_path"])
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    state["document_text"] = text
    state["logs"].append("PDF Loaded Successfully")
    print("Exiting Ingestion")
    return state