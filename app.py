import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 Resume Analyzer with ATS Score")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description Here")

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume uploaded successfully!")

    if job_desc:
        resume_words = set(resume_text.lower().split())
        job_words = set(job_desc.lower().split())

        matched = resume_words.intersection(job_words)
        missing = job_words - resume_words

        score = (len(matched) / len(job_words)) * 100 if job_words else 0

        st.subheader(f"🎯 ATS Score: {score:.2f}%")

        st.write("### ✅ Matched Keywords")
        st.write(list(matched)[:20])

        st.write("### ❌ Missing Keywords")
        st.write(list(missing)[:20])
