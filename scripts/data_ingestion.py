import json
import time
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ==========================
# Clean Text
# ==========================
def clean_text(doc):
    text = doc.page_content.encode(
        "utf-8",
        "ignore"
    ).decode("utf-8")

    doc.page_content = text
    return doc


# ==========================
# Load JSON
# ==========================

with open(
    r"data/langchain_rag_docs.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

documents = []

for item in data:
    documents.append(
        Document(
            page_content=item["content"],
            metadata={
                "source": item["url"]
            }
        )
    )

print(f"Length of documents: {len(documents)}")
print("Documents Created")


# ==========================
# Chunking
# ==========================
chunk_size = 3000
chunk_overlap = 100

splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

chunks = splitter.split_documents(documents)

cleaned_chunks = [
    clean_text(chunk)
    for chunk in chunks
]

print("Chunks Created")
print(f"Total Chunks: {len(cleaned_chunks)}")

total_chars = sum(
    len(doc.page_content)
    for doc in documents
)

print(f"Total Characters: {total_chars:,}")


# ==========================
# Embeddings
# ==========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Created")

print("Testing embedding model...")

start = time.time()

test_embedding = embeddings.embed_query(
    "hello world"
)

print(
    f"Embedding Dimension: "
    f"{len(test_embedding)}"
)

print(
    f"Embedding Test Time: "
    f"{time.time()-start:.2f} sec"
)


# ==========================
# Build FAISS
# ==========================
try:
    batch_size = 100

    print("Creating FAISS Index...")

    first_batch = cleaned_chunks[:batch_size]

    db = FAISS.from_documents(
        first_batch,
        embeddings
    )

    print("First batch completed")

    for i in range(batch_size, len(cleaned_chunks), batch_size):

        batch = cleaned_chunks[i:i+batch_size]

        try:
            db.add_documents(batch)
            print(f"Added {i} -> {i+len(batch)}")

        except Exception as e:
            print(f"FAILED at batch starting {i}")
            print(e)
            break

    db.save_local(
        r"C:\GenAi\LangBot\faiss_index"
    )

except Exception as e:
    print("\nERROR OCCURRED")
    print(str(e))


retriever = db.as_retriever(
        search_kwargs={"k": 4}
    )


response= retriever.invoke("What is the LCEL")

print("The response is ",response)