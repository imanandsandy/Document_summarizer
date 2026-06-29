from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunking_agent(state):
    print("Entering Chunking")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=100
    )
    chunks = splitter.split_text(
        state["document_text"]
    )
    print(f"Total Chunks Created: {len(chunks)}")
    state["chunks"] = chunks

    state["logs"].append(
        f"{len(chunks)} chunks created"
    )
    print(f"Created {len(chunks)} chunks")
    print("Existing Chunking")
    return state