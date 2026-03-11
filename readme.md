# Vectorless PDF Question Answering System

A lightweight **Vectorless Retrieval-Augmented Generation (RAG)** system that allows users to ask questions from a PDF document.

Unlike traditional RAG systems, this project **does not use embeddings or vector databases**. Instead it uses **BM25 keyword retrieval** to find relevant sections from the document and then sends them to an LLM to generate answers.

This makes the system **cheaper, faster, and simpler to run locally**.

---

## Features

- PDF text extraction  
- Section-based document parsing  
- Vectorless retrieval using BM25  
- Question answering using a local LLM  
- Lightweight and fast  
- No embedding costs  
- No vector database required  

---

## Architecture

```
PDF
 └─ Text Extraction (pdfplumber)
     └─ Section Parser
         └─ Tokenization (NLTK)
             └─ BM25 Index
                 └─ Query Retrieval
                     └─ Context Builder
                         └─ LLM Answer
```

---

## Project Structure

```
vectorless-learn/
│
├── main.py
├── parser.py
├── bm25_index.py
├── bm25_retriever.py
├── qa_engine.py
├── oral_cancer.pdf
└── README.md
```

---

## Installation

Install dependencies:

```
pip install pdfplumber nltk rank-bm25 ollama
```

Download required NLTK resources:

```
python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

---

## Running the System

Run the application:

```
python main.py
```

Example interaction:

```
Ask a question:
How does autofluorescence detect oral cancer?

Answer:
Autofluorescence visualization helps detect abnormal tissue
changes in the oral cavity that may not be visible under
conventional white-light examination.
```

---

## How It Works

1. Text Extraction  
   Extract text from the PDF using pdfplumber.

2. Section Parsing  
   Split the document into logical sections.

3. BM25 Index  
   Tokenize text and build a BM25 retrieval index.

4. Query Retrieval  
   Retrieve top relevant sections using BM25 ranking.

5. Context Builder  
   Combine retrieved sections into context.

6. LLM Answer  
   Send context and query to an LLM to generate the final answer.

---

## Advantages of Vectorless Retrieval

- No embedding generation
- No vector database
- Faster indexing
- Lower infrastructure cost
- Deterministic retrieval

---

## Limitations

- Keyword-based retrieval
- Less semantic understanding than embedding search
- Retrieval quality depends on token matching

---

## Future Improvements

- Multi-PDF support
- Persistent index storage
- Streamlit UI
- Metadata filtering
- Hybrid retrieval (keyword + semantic)

---

## Technologies Used

- Python
- pdfplumber
- NLTK
- rank-bm25
- Ollama

---

## Example Use Cases

- Research paper analysis
- Medical document QA
- Legal document search
- Technical documentation assistant

---

## License

MIT License