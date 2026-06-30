import streamlit as st

st.set_page_config(
    page_title="Lightweight Document QA",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Lightweight Document QA")
st.write("Ask questions about your document.")

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("Processing...")
        st.write("Your answer will appear here.")