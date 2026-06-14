import json



with open(r"C:\GenAi\LangBot\Data Collection\langchain_document.json","r",encoding="utf-8") as file:
    data = json.load(file)

keep_keywords = [
    "rag",
    "retrieval",
    "retriever",
    "vectorstore",
    "vectorstores",
    "embedding",
    "embeddings",
    "text-splitter",
    "text_splitters",
    "document-loader",
    "document_loaders",
    "prompt-template",
    "prompt_templates",
    "chat-model",
    "chat_models",
    "output-parser",
    "output_parsers",
    "runnable",
    "lcel",
    "chatbot",
    "tutorial"
]

filtered_docs = []

for item in data:
    url = item["url"].lower()

    if any(keyword in url for keyword in keep_keywords):
        filtered_docs.append(item)

print(f"Original Docs: {len(data)}")
print(f"Filtered Docs: {len(filtered_docs)}")

with open(
    r"C:\GenAi\LangBot\Data Collection\langchain_rag_docs.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        filtered_docs,
        file,
        ensure_ascii=False,
        indent=2
    )

print("Filtered JSON saved successfully")