import pdfplumber
from parse import split_sections
from bm25_index import build_bm25
from bm25_retriever import retrieve_bm25
from QA_engine import generate_answer

# extract text
text = ""
with pdfplumber.open("/home/user171125/Downloads/vectorless-learn/autofluorescence-1.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"

# parse sections
sections = split_sections(text)

# build bm25 index
bm25, corpus = build_bm25(sections)

while True:

    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        break

    results = retrieve_bm25(query, bm25, corpus, sections)

    context = ""

    for r in results:
        context += r["content"][:800] + "\n\n"

    answer = generate_answer(query, context)

    print("\nAnswer:\n")
    print(answer)