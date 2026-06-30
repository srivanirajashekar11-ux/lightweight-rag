import json

# Load extracted sections once
with open("extracted/sections.json", "r", encoding="utf-8") as f:
    SECTIONS = json.load(f)


def retrieve(question: str):
    """
    Returns the most relevant section based on keyword overlap.
    """

    question_words = set(question.lower().split())

    best_section = None
    best_score = -1

    for section in SECTIONS:
        text = section["content"].lower()

        # simple scoring: count matching words
        score = sum(word in text for word in question_words)

        if score > best_score:
            best_score = score
            best_section = section

    return best_section