def retrieve(query, index, sections):

    query_words = query.lower().split()

    results = set()

    for word in query_words:
        if word in index:
            results.update(index[word])

    retrieved_sections = [sections[i] for i in results]

    return retrieved_sections