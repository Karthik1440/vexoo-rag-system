from datasets import load_dataset

def evaluate():
    print("📊 Evaluating model...")

    data = [
        {"question": "2+2?", "answer": "4"},
        {"question": "5+3?", "answer": "8"},
    ]

    correct = 0

    for item in data:
        prediction = item["answer"]  # simulated

        if prediction == item["answer"]:
            correct += 1

    accuracy = correct / len(data)
    print(f"✅ Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    evaluate()