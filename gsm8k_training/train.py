from datasets import load_dataset

def load_data():
    print("📥 Loading GSM8K dataset (simulated)...")

    data = [
        {"question": "If you have 2 apples and buy 3 more, how many apples?", "answer": "5"},
        {"question": "What is 10 minus 4?", "answer": "6"},
        {"question": "If a car travels 60 km in 1 hour, how far in 2 hours?", "answer": "120"},
    ]

    return data


def tokenize_data(data):
    print("🔤 Tokenizing data...")

    tokenized = []
    for item in data:
        tokenized.append({
            "input": item["question"],
            "output": item["answer"]
        })

    return tokenized


def train():
    data = load_data()
    data = tokenize_data(data)

    print("🤖 Initializing model (simulated)...")

    print("🚀 Training started...")
    for epoch in range(3):
        print(f"Epoch {epoch+1}/3 running...")

    print("✅ Training complete")


if __name__ == "__main__":
    train()