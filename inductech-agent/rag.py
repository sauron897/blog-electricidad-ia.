from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import PyPDF2

DOCS_DIR = Path("docs")
CHROMA_DIR = ".chroma_db"
_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)


def _get_store() -> Chroma:
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=OpenAIEmbeddings())


def get_retriever():
    """Returns a retriever backed by Chroma. Loads docs/ folder on first run."""
    store = _get_store()
    if store._collection.count() == 0:
        DOCS_DIR.mkdir(exist_ok=True)
        docs = []
        for pdf in DOCS_DIR.glob("**/*.pdf"):
            docs.extend(PyPDFLoader(str(pdf)).load())
        for txt in DOCS_DIR.glob("**/*.txt"):
            docs.extend(TextLoader(str(txt), encoding="utf-8").load())
        if docs:
            store.add_documents(_splitter.split_documents(docs))
    return store.as_retriever(search_kwargs={"k": 4})


def ingest_uploaded_files(uploaded_files) -> int:
    """Ingest Streamlit uploaded files into the vector store. Returns number of docs added."""
    store = _get_store()
    documents = []
    for f in uploaded_files:
        if f.type == "application/pdf":
            reader = PyPDF2.PdfReader(f)
            text = "".join(page.extract_text() or "" for page in reader.pages)
            documents.append(Document(page_content=text, metadata={"source": f.name}))
        elif f.type == "text/plain":
            documents.append(Document(
                page_content=f.getvalue().decode("utf-8"),
                metadata={"source": f.name}
            ))
    if documents:
        store.add_documents(_splitter.split_documents(documents))
    return len(documents)
