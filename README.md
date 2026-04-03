# RAG System

A lightweight local Retrieval-Augmented Generation (RAG) project for indexing Markdown and text documents, retrieving relevant chunks with vector search, and generating grounded answers with an LLM.

This repository is built around:

- Sentence Transformers for embeddings
- ChromaDB for persistent vector storage
- Ollama for local chat-based generation
- A simple CLI for indexing, search, and question answering

## What It Does

The application reads files from `data/documents`, chunks them based on file type, stores embeddings in ChromaDB, and answers questions using retrieved context.

Current flow:

1. Load `.md` and `.txt` documents from `data/documents`
2. Chunk content with plain-text or markdown-aware chunking
3. Create embeddings with a Sentence Transformers model
4. Store vectors in a persistent ChromaDB collection under `data/chroma_db`
5. Expand user questions into multiple retrieval queries
6. Retrieve relevant chunks and send them to the LLM for the final answer

## Features

- Local-first RAG workflow
- Supports `.md` and `.txt` files
- Markdown-aware chunking for structured docs
- Persistent ChromaDB storage
- Incremental indexing using file content hashes
- Semantic search over indexed chunks
- Multi-query retrieval step before answer generation
- CLI interface with `index`, `search`, and `ask` commands

## Project Structure

```text
rag-system/
├── data/
│   ├── chroma_db/          # Persistent ChromaDB data
│   └── documents/          # Source documents to index
├── src/
│   ├── core/
│   │   ├── llm/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── utils.py
│   ├── chunker.py
│   ├── ingest.py
│   ├── query.py
│   └── query_translator.py
├── main.py
├── pyproject.toml
└── .env.example
```

## Requirements

- Python 3.10+
- Poetry
- Ollama installed and running locally

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rag-system
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Create your environment file

```bash
cp .env.example .env
```

Update `.env` as needed:

```env
LLM_PROVIDER=ollama
HF_EMBEDDINGS_MODEL=all-MiniLM-L6-v2
OLLAMA_LLM_MODEL=qwen3.5:0.8b
COLLECTION_NAME=ims-manual
```

Notes:

- `LLM_PROVIDER` should be set. The current implementation expects a value such as `ollama`.
- `OLLAMA_LLM_MODEL` must match a model available in your local Ollama instance.
- `COLLECTION_NAME` controls the ChromaDB collection used for indexing and search.

### 4. Pull an Ollama model

```bash
ollama pull qwen3.5:0.8b
```

### 5. Run commands through Poetry

```bash
poetry run python main.py <command>
```

Using `poetry run` helps ensure the required Python packages are available.

## Usage

### Index documents

Reads files from `data/documents`, chunks them, creates embeddings, and stores them in ChromaDB.

```bash
poetry run python main.py index
```

### Search the vector database

Runs semantic retrieval only and prints matching chunks with metadata.

```bash
poetry run python main.py search -q "refund policy"
```

Optional arguments:

- `-k`, `--top-k` to control the number of retrieved results

Example:

```bash
poetry run python main.py search -q "return policy" -k 5
```

### Ask a question

Runs the retrieval pipeline and sends retrieved context to the LLM.

```bash
poetry run python main.py ask -q "What does the manual say about inspections?"
```

Optional arguments:

- `-k`, `--top-k` is accepted by the CLI, though the current retrieval path does not fully use that value end-to-end

## How Indexing Works

### Plain text files

Plain text documents are split into overlapping chunks. The chunker tries to end chunks at sentence boundaries when possible.

### Markdown files

Markdown documents are split more carefully:

- Top-level structure is preserved
- `##` sections are used as natural boundaries
- Small sections may be combined
- Large sections may be split by paragraphs

## How Querying Works

When you run `ask`:

1. Your question is sent to a query translator prompt
2. The LLM generates multiple alternate phrasings
3. Each phrasing is searched against ChromaDB
4. Retrieved chunks are deduplicated
5. The final context is passed to the LLM for answer generation

This improves recall compared with a single vector search query.

## Supported File Types

- `.md`
- `.txt`

Files should be placed in:

```text
data/documents/
```

## Example Workflow

```bash
poetry run python main.py index
poetry run python main.py search -q "audit requirements"
poetry run python main.py ask -q "What are the audit requirements?"
```

## Configuration Reference

Environment variables currently used by the code:

- `LLM_PROVIDER`
- `HF_EMBEDDINGS_MODEL`
- `OLLAMA_LLM_MODEL`
- `COLLECTION_NAME`

Defaults are defined in `src/core/config.py` for some values, but `LLM_PROVIDER` should still be set explicitly.

## Current Limitations

- Ollama is the only implemented chat backend right now
- `OpenAIChatModel` exists as a placeholder and is not implemented
- The `index` command accepts `--documents-path`, but the current ingestion code still reads from `data/documents`
- Some CLI help text and code paths are still evolving

## Development

Dev dependencies included in the project:

- `pytest`
- `black`
- `ruff`

Install them with Poetry and run tools from the project environment:

```bash
poetry run ruff check .
poetry run black .
poetry run pytest
```

## Troubleshooting

### `ModuleNotFoundError`

If you run `python main.py ...` directly and dependencies are missing, use:

```bash
poetry run python main.py <command>
```

### No answer or poor retrieval

Check the following:

- Documents were indexed successfully
- The Ollama model is installed and available locally
- `LLM_PROVIDER=ollama` is set in `.env`
- `COLLECTION_NAME` matches the collection you indexed into
