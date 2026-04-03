# 🧠 Vexoo AI Engineer Assignment

## 📌 Overview
This project implements a Retrieval-Augmented Generation (RAG) system with a Knowledge Pyramid architecture and a simulated GSM8K reasoning model training pipeline.

---

## 🚀 Features

### ✅ Part 1: RAG System
- Sliding window document chunking
- Knowledge Pyramid with 4 layers:
  - Raw Text
  - Summary
  - Category Label
  - Keywords
- Semantic search using TF-IDF + cosine similarity
- Interactive UI using Streamlit

---

### ✅ Part 2: GSM8K (Reasoning Model)
- Loaded GSM8K dataset
- Tokenization pipeline (simulated)
- Training loop (simulated)
- Evaluation using accuracy metric

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn (TF-IDF)
- HuggingFace Datasets

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit scikit-learn dataset
Run RAG UI

streamlit run app.py

>>Run GSM8K training
python gsm8k_training/train.py
>> Run evaluation
python gsm8k_training/evaluate.py

streamlit run app.py
