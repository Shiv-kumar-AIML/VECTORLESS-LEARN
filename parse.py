import re

def split_sections(text):

    sections = re.split(r'\n[A-Z][A-Za-z ]+\n', text)

    structured_sections = []

    for i, sec in enumerate(sections):
        structured_sections.append({
            "id": i,
            "content": sec.strip()
        })

    return structured_sections