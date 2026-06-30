import os
import json
import pymupdf4llm

# Input PDF path (your file)
PDF_FILE = "docs/Introduction_to_AI.pdf"

# Output JSON file
OUTPUT_FILE = "extracted/sections.json"

def extract_pdf_to_sections(pdf_path):
    print(f"Extracting content from: {pdf_path}")

    # Convert PDF → Markdown using PyMuPDF4LLM
    markdown = pymupdf4llm.to_markdown(pdf_path)

    sections = []
    current_title = "Introduction"
    current_content = []

    for line in markdown.splitlines():
        line = line.strip()

        if not line:
            continue

        # Detect headings
        if line.startswith("#"):
            # Save previous section
            if current_content:
                sections.append({
                    "title": current_title,
                    "content": "\n".join(current_content).strip()
                })

            # Start new section
            current_title = line.lstrip("#").strip()
            current_content = []
        else:
            current_content.append(line)

    # Save last section
    if current_content:
        sections.append({
            "title": current_title,
            "content": "\n".join(current_content).strip()
        })

    return sections


def save_sections(sections, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=4, ensure_ascii=False)

    print(f"\nExtraction completed successfully!")
    print(f"Total sections: {len(sections)}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    if not os.path.exists(PDF_FILE):
        print(f"ERROR: File not found → {PDF_FILE}")
        print("Check filename inside docs/ folder using: ls docs")
        exit(1)

    sections = extract_pdf_to_sections(PDF_FILE)
    save_sections(sections, OUTPUT_FILE)