
### Project Title

**RAG-app** – Your chill AI buddy for retrieval-augmented generation, running smooth on Streamlit

---

### What’s This?

RAG-app is your dope Streamlit-based RAG system that lets you build slick AI apps using documents or datasets. Handles all that vector-store integration and LLM orchestration — all in a sleek, shareable web UI. Perfect for creating tools, search, knowledge assistants, or any smart interface on top of your data.

---

### Features

* **Streamlit-powered UI** — Frontend that’s fast, clean, and hella user-friendly.
* **Retrieval + Generation** — Combines vector retrieval (Chroma, FAISS, etc.) with LLMs to answer smartly.
* **Flexible vector backend** — Easily switch between different vector stores (Chroma if you install `chromadb`, or fallback to FAISS).
* **Cloud-native** — Deploys out-of-the-box on Streamlit Community Cloud with your lock file.
* **Simple environment setup** — Manage dependencies with `uv`, `pyproject.toml`, or your preferred method.

---

### Prereqs

* Python 3.12 (same as in logs)
* Use `uv` (preferred), or `pip` / `poetry`
* Optional: `chromadb` if you want Chroma; otherwise, Python's built-in `sqlite3` or FAISS will work.

---

### Getting Started

1. Clone it:

   ```bash
   git clone https://github.com/FazeelAr/RAG-app.git
   cd RAG-app
   ```

2. Set up environment:

   * With `uv`:

     ```bash
     uv install
     ```
   * Or with `pip`:

     ```bash
     pip install -r requirements.txt
     ```

3. (Optional) Add Chroma for better vector store support:

   ```bash
   uv add chromadb
   ```

4. Launch the app:

   ```bash
   streamlit run main.py
   ```

5. Open the UI in your browser, drag docs, ask questions, and let the LLM do its magic.

---

### Project Structure

| Folder/File                                     | Purpose                                                                       |
| ----------------------------------------------- | ----------------------------------------------------------------------------- |
| `main.py`                                       | Entry point—sets up Streamlit UI and triggers the ingestion+LLM flow.         |
| `src/`                                          | Core logic like `vector_store.py`, data loading, and RAG orchestration.       |
| `config/`, `data/`                              | Optional zones for storing configs or sample data; tweak as per your setup.   |
| `.devcontainer/`                                | Setup for reproducible dev environment (VS Code friendly!).                   |
| `uv.lock`, `requirements.txt`, `pyproject.toml` | Dependency management tools. Keep one consistent method—`uv.lock` is default. |

---

### Tips & Best Practices

* If `pysqlite3` causes headaches (like missing Windows wheels), just use:

  ```python
  import sqlite3
  ```

  Works everywhere, no stress.

* Want to switch to FAISS? In your vector setup:

  ```python
  from langchain_community.vectorstores import FAISS
  ```

  It's zero-dependency and cloud-friendly.

* Lock file clutter? Clean up by:

  ```bash
  uv remove problematic-package
  uv add chromadb  # for vector persistence
  ```

---

### Why RAG-app?

Because generative AI is cooler when it's grounded in your own data. This repo is your launchpad—super customizable, perfectly so for research tools, chatbots with memory, or knowledge assistants.

Share it, remix it, deploy it — and watch AI get way smarter.
