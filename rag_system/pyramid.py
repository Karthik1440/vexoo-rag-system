from rag_system.utils import summarize, categorize, extract_keywords
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def build_pyramid(chunks):
    knowledge_base = []

    # Fit vectorizer on all chunks
    vectors = vectorizer.fit_transform(chunks)

    for i, chunk in enumerate(chunks):
        pyramid = {
            "raw_text": chunk,
            "summary": summarize(chunk),
            "label": categorize(chunk),
            "keywords": extract_keywords(chunk),
            "embedding": vectors[i]
        }
        knowledge_base.append(pyramid)

    return knowledge_base, vectorizer