import streamlit as st
import requests

st.set_page_config(
    page_title="Agentic Document Summarizer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Agentic Document Summarizer")
st.write("Upload a PDF and generate an AI-powered summary using LangGraph + Qwen.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"Selected File: {uploaded_file.name}")

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            "application/pdf"
                        )
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    st.subheader("📌 Summary")
                    st.write(result["summary"])

                    st.subheader("📊 Quality Score")
                    st.metric(
                        label="Score",
                        value=result["quality_score"]
                    )

                    st.subheader("⚙️ Workflow Logs")

                    for log in result["logs"]:
                        st.write(f"✅ {log}")

                else:
                    st.error(
                        f"API Error: {response.status_code}"
                    )

            except Exception as e:
                st.error(str(e))