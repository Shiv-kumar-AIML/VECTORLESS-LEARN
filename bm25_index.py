from rank_bm25 import BM25Okapi
import nltk

def build_bm25(sections):

    corpus = []

    for sec in sections:
        tokens = nltk.word_tokenize(sec["content"].lower())
        corpus.append(tokens)

    bm25 = BM25Okapi(corpus)

    return bm25, corpus