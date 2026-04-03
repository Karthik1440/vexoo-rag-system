from rag_system.ingestion import sliding_window
from rag_system.pyramid import build_pyramid
from rag_system.retrieval import retrieve

def load_document():
    return """AI is transforming healthcare and finance industries. 
    Machine learning helps in predictive analytics. 
    Finance sectors use AI for fraud detection. 
    Healthcare uses AI for diagnosis and patient care."""

def main():
    print("📄 Loading document...")
    text = load_document()

    print("✂️ Creating chunks...")
    chunks = sliding_window(text)

    print("🏗️ Building knowledge pyramid...")
    kb = build_pyramid(chunks)

    while True:
        query = input("\n🔍 Enter your query (or 'exit'): ")
        if query.lower() == "exit":
            break

        result = retrieve(query, kb)

        if result:
            # 🔥 Instead of only one layer → show full info
            print("\n✅ Result Found:\n")
            print("📄 Summary:", result.get("summary"))
            print("🏷️ Category:", result.get("label"))
            print("🔑 Keywords:", result.get("keywords"))
            print("\n📚 Raw Text:\n", result.get("raw_text"))
        else:
            print("❌ No result found.")

if __name__ == "__main__":
    main()