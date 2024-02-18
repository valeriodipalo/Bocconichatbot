# Imports main tools:
from trulens_eval import TruChain, Feedback, Huggingface, Tru
from trulens_eval.schema import FeedbackResult
tru = Tru()
tru.reset_database()

# Imports from langchain to build app
import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough

from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from langchain.memory import ConversationBufferMemory

from langchain.chains import StuffDocumentsChain,LLMChain,ReduceDocumentsChain,MapReduceDocumentsChain

from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

import json
import os
import textwrap
from getpass import getpass
from pathlib import Path

import chromadb
import langchain
import openai
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import (
    ChatMessageHistory,
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryBufferMemory,
    VectorStoreRetrieverMemory,)

from langchain.prompts.prompt import PromptTemplate
from langchain.schema import messages_from_dict, messages_to_dict
from langchain.vectorstores import Chroma


import langchain 
print(langchain.__version__) 

import trulens_eval
print(trulens_eval.__version__)

import openai 
print(openai.__version__) #version update 

import os 
os.environ["OPENAI_API_KEY"] = "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"
os.environ["LANGCHAIN_API_KEY"] = "ls__a7cd2e593e7248e594ac5b698bae1f7c"

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] ="Bocconi-chat"

### LOAD 
path_full_p = "../../Data/New/Markdown/Full_plain.md"
headers_to_split_on_plain = [
    ("#", "Category"),
    ("##", "Subcategory"),
    ("###", "Question"),
    ("####", "URL"),
    ("#####", "ID"), 
]




    
    