from sklearn.metrics.pairwise import cosine_similarity

def retrieve(query, knowledge_base, vectorizer):
    query_vector = vectorizer.transform([query])

    best_score = -1
    best_item = None

    for item in knowledge_base:
        score = cosine_similarity(query_vector, item["embedding"])[0][0]

        if score > best_score:
            best_score = score
            best_item = item

    return best_item, best_score