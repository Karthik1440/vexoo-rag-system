def sliding_window(text, window_size=1000, overlap=200):
    chunks = []
    for i in range(0, len(text), window_size - overlap):
        chunk = text[i:i + window_size]
        if chunk:
            chunks.append(chunk)
    return chunks