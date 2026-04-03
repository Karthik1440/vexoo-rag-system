from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def summarize(text):
    summary = text[:150]
    
    # avoid cutting mid-word
    if " " in summary:
        summary = summary.rsplit(" ", 1)[0]
    
    return summary + "..."

def categorize(text):
    text = text.lower()
    if "finance" in text:
        return "Finance"
    elif "health" in text:
        return "Healthcare"
    elif "ai" in text:
        return "Technology"
    else:
        return "General"

def extract_keywords(text):
    words = list(set(text.lower().split()))
    return words[:10]

def extract_keywords(text):
    words = text.lower().replace(".", "").replace(",", "").split()
    
    stopwords = {"and", "is", "in", "the", "for", "of", "to"}
    
    keywords = [w for w in set(words) if w not in stopwords]
    
    return keywords[:10]