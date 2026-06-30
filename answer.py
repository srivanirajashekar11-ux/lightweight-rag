from llama_cpp import Llama
from retrieve import retrieve

# Load local model
llm = Llama(
    model_path="models/qwen2.5-3b-instruct-q4_k_m.gguf",
    n_ctx=4096,
    n_threads=8,
    verbose=False
)

SYSTEM_PROMPT = """
You are a strict document QA assistant.

Rules:
- Answer ONLY from the given section
- If answer is not in the section, say "Not found in document"
- Do not hallucinate
"""

while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    section = retrieve(question)

    if not section:
        print("No relevant section found.")
        continue

    prompt = f"""
{SYSTEM_PROMPT}

SECTION TITLE:
{section['title']}

SECTION CONTENT:
{section['content']}

QUESTION:
{question}

ANSWER:
"""

    response = llm(
        prompt,
        max_tokens=256,
        temperature=0.2
    )

    print("\n--- RESPONSE ---\n")
    print(response["choices"][0]["text"].strip())