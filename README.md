# RAG System (Retrieval-Augmented Generation)

A lightweight **Retrieval-Augmented Generation (RAG)** system built with:

- Sentence Transformers (Embeddings)
- ChromaDB (Vector Database)
- Ollama (Local LLM inference)
- Markdown/Text document ingestion
- CLI-based interface

This project lets you:
- Index documents into a vector database
- Search semantically across files
- Ask questions and get AI-generated answers grounded in your documents

---

# Features

- Load `.txt` and `.md` documents automatically
- Smart markdown-aware chunking
- Embedding-based semantic search
- Persistent ChromaDB storage
- Local LLM answers using Ollama (no API required)
- CLI commands for indexing, search, and Q&A
- Incremental indexing using file hashing

---

# Installation

## 1. Clone repository

```bash
git clone https://github.com/your-username/rag-system.git
cd rag-system
```


## 2. Install Poetry (if not installed)

```bash
pip install poetry
```

Or:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 3. Install dependencies

```bash
poetry install
```

## 4. Activate environment
```bash
poetry shell
```

## 5. Install and run Ollama
Download [Ollama](https://ollama.com) and install it. After installing you will be to run following command and pull LLM model. You can pull model of your own choice as well.

```bash
ollama pull qwen3.5:0.8b
```

## 5. Create .env
Make sure to create `.env` file before running any script. There are variables for LLM Models, Embedding Models etc.

```bash
cp .env.example .env
```

# Usage

## Build index (ingest documents)

```bash
poetry run python main.py index
```

This will:

- Read all documents
- Chunk them
- Generate embeddings
- Store them in ChromaDB

## Search documents (no LLM)
```bash
python main.py search -q "your query" -k 3
```
Example:
```bash
python main.py search -q "refund policy"
```

## Ask questions (RAG mode)
```bash
python main.py query -q "your question"
```
Example:
```bash
python main.py query -q "What is the return policy?"
```