import pdfplumber

pdf_path = "/home/user171125/Downloads/vectorless-learn/autofluorescence-1.pdf"

text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"

print(text[:1000])

