import nltk

def retrieve_bm25(query, bm25, corpus, sections, top_k=3):

    query_tokens = nltk.word_tokenize(query.lower())

    scores = bm25.get_scores(query_tokens)

    ranked_ids = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    results = [sections[i] for i in ranked_ids[:top_k]]

    return results