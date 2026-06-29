# 📄 Agentic AI Document Summarization System

An Agentic AI-based document summarization system that processes PDF documents using a multi-agent workflow orchestrated by **LangGraph**. The system extracts text, generates chunk-level summaries, evaluates the quality of the generated summary, and conditionally refines it before returning the final executive summary.

---

## 🚀 Features

- 📄 PDF Upload and Processing
- 🤖 Multi-Agent Workflow using LangGraph
- 📝 Chunk-based Document Summarization
- 📊 Quality Evaluation of Generated Summary
- 🔄 Conditional Summary Refinement
- 🧠 Local LLM using Ollama (Qwen 2.5 3B)
- ⚡ FastAPI Backend
- 🎨 Streamlit Frontend

---

# 🏗️ System Architecture

<img width="1536" height="1024" alt="tcs_project" src="https://github.com/user-attachments/assets/93f2f619-1a8f-4f56-8fc6-cb36e9bd56dc" />






# 🔄 Workflow

The workflow consists of multiple specialized agents coordinated using LangGraph.

```
User Uploads PDF
        │
        ▼
 Ingestion Agent
        │
        ▼
 Chunking Agent
        │
        ▼
 Summarizer Agent
        │
        ▼
 Aggregator Agent
        │
        ▼
 Evaluator Agent
        │
        ▼
Decision Router
   │            │
   │            ▼
   │        Final Output
   │
   ▼
Refiner Agent
   │
   ▼
Final Output
```

---

# 🧩 Agent Responsibilities

### 📥 Ingestion Agent

- Reads uploaded PDF
- Extracts text using PyPDF
- Stores extracted content in the shared state

---

### ✂️ Chunking Agent

- Splits large documents into manageable chunks
- Uses RecursiveCharacterTextSplitter
- Prevents exceeding the LLM context window

---

### 📝 Summarizer Agent

- Processes each chunk individually
- Generates concise summaries using Qwen 2.5 3B via Ollama

---

### 📚 Aggregator Agent

- Combines all chunk summaries
- Produces a consolidated executive summary

---

### 📊 Evaluator Agent

- Evaluates the generated summary
- Assigns a quality score (1–10)
- Acts as the decision point of the workflow

---

### ✨ Refiner Agent

- Triggered only if the quality score is below the threshold
- Improves readability, clarity, and conciseness
- Returns the refined summary

---

# 🧠 State Management

LangGraph maintains a shared state across all agents.

```python
SummaryState
│
├── pdf_path
├── document_text
├── chunks
├── chunk_summaries
├── final_summary
├── quality_score
└── logs
```

Each agent reads from and writes to this shared state, enabling seamless communication throughout the workflow.

---

# 🔀 Decision Flow

```
Evaluator Agent
        │
        ▼
Quality Score
        │
        ▼
 Is Score < Threshold?
      │         │
      │         ▼
      │      Return Summary
      ▼
Refiner Agent
      │
      ▼
Improved Summary
```

This conditional routing makes the workflow **agentic**, allowing the system to decide dynamically whether refinement is required.

---

# 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Workflow | LangGraph |
| LLM | Qwen 2.5 3B (Ollama) |
| PDF Processing | PyPDF |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |

---

# 📂 Project Structure

```
agentic-document-summarizer/

├── frontend/
│   └── app.py
│
├── backend/
│   ├── main.py
│   ├── llm.py
│   ├── state.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   └── agents/
│       ├── ingestion.py
│       ├── chunking.py
│       ├── summarizer.py
│       ├── aggregator.py
│       ├── evaluator.py
│       └── refiner.py
│
├── uploads/
│
└── README.md
```

---

# ▶️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd agentic-document-summarizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Pull Ollama Model

```bash
ollama pull qwen2.5:3b
```

### Start Ollama

```bash
ollama serve
```

### Run Backend

```bash
python -m uvicorn backend.main:app --reload
```

### Run Frontend

```bash
python -m streamlit run frontend/app.py
```

---

# 📌 Future Improvements

- Parallel chunk summarization
- Support for larger PDF documents
- Multiple LLM support
- Caching previously summarized documents
- Better evaluation metrics (ROUGE/BERTScore)
- Streaming responses
- Multi-document summarization

---

# 📜 License

This project is developed for educational and demonstration purposes.
