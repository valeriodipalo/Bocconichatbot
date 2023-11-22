import Chroma
vectordb = Chroma.from_documents(
    documents=md_header_splits,
    embedding=embedding,
    persist_directory=persist_directory
)
