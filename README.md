# CasaDeAnza — RAG Demo (casadeanza)

This repository contains a small Retrieval-Augmented Generation (RAG) example built around a CasaDeAnza policy document collection. It demonstrates document ingestion, PDF reading, chunking, vector storage, vector search, context augmentation, and response generation.

**Quick overview**

- `utils.py`: helpers to find and read PDFs (`read_casadeanza_docs`, `read_pdf`, etc.).
- `complete_rag_pipeline_demo.py`: end-to-end demo showing load → chunk → store → query → generate.
- `save_vector_db.py`: saves documents/ids to a persistent ChromaDB and writes a backup JSON.
- `overlap_chunking.py`: demo showing effect of chunk overlap when splitting text.
- `casadeanza-proj/`: place your PDF policy files here (project already includes sample PDFs).

**Requirements**

- Python 3.10+ (3.11 recommended)
- Install dependencies:

```bash
pip install -r requirements.txt
```

**Setup & Usage**

1. Place PDFs in `casadeanza-proj/` (the project already includes several PDFs). The utilities read all `*.pdf` files there.

2. Run the complete demo (this will chunk documents, create embeddings, and simulate LLM responses):

```bash
python complete_rag_pipeline_demo.py
```

3. Save the vector DB (loads docs via `read_casadeanza_docs`) and write a JSON backup:

```bash
python save_vector_db.py
```

4. Quick chunking demo (uses the first loaded document or an embedded fallback):

```bash
python overlap_chunking.py
```

**Notes**

- `utils.read_casadeanza_docs()` returns `(docs, paths)` where `docs` are extracted PDF text strings and `paths` are the PDF file paths.
- The demos use `SentenceTransformer('all-MiniLM-L6-v2')` for embeddings by default—install `sentence-transformers`.
- ChromaDB files are stored in `./chroma_db/` by default in these scripts.

**Repository**

- Pushed to: https://github.com/desran/rag-ex

**Next steps / tips**

- Replace the simulated LLM in `generate_response()` with a real API call.
- Tune chunk sizes/overlap in `complete_rag_pipeline_demo.py` for best retrieval quality.

---

If you want, I can also add a `Makefile` or `run_demo.sh` to simplify running the demos.
