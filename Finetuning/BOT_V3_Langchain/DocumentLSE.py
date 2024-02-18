import os
import openai
import sys
import numpy as np
import pandas as pd
import sys
#1
from langchain.document_loaders import UnstructuredMarkdownLoader
#2
from langchain.document_loaders import NotionDirectoryLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
#3
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# SET UP #
sys.path.append('../..')
os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

# 1. DOCUMENT LOADING #
file_path = "../../Data/Scraping_Bocconi_converted_no_dup_check.md"
with open(file_path, 'r') as file:
    markdown_content = file.read()

# 2. DOCUMENT SPLITTING #
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),]
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on)
splits = markdown_splitter.split_text(markdown_content)

# 3. VECTOR STORE AND EMBEDDING
!rm -rf ./docs/chroma
persist_directory = 'docs/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory)

vectordb.persist()
vectordb = None
