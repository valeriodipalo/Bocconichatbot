import os
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma


os.environ["OPENAI_API_KEY"] = "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"
os.environ["LANGCHAIN_API_KEY"] = "ls__a7cd2e593e7248e594ac5b698bae1f7c"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] ="Bocconi-chat"
path_full_p = "S3_files/Full_plain.md"
headers_to_split_on_plain = [
    ("#", "Category"),
    ("##", "Subcategory"),
    ("###", "Question"),
    ("####", "URL"),
    ("#####", "ID"), 
]


with open(path_full_p, 'r') as file:
    markdown_content = file.read()

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on_plain)
splits = markdown_splitter.split_text(markdown_content)

embedding=OpenAIEmbeddings() #

llm_name = "gpt-3.5-turbo" #
llm = ChatOpenAI(model_name=llm_name, temperature=0) #

#vs_full_plain = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(),persist_directory="./chroma_db" )
db3 = Chroma(embedding_function=embedding, persist_directory="S3_files/chroma_db")

#ret_full_plain = vs_full_plain.as_retriever()
ret_full_plain = db3.as_retriever()


template = """
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
If you the question is too broad and could lead to multiple answers ask the user for clarifications.
Keep the answer as concise as possible.
Be exhaustive if the user is asking for it. 
For text provided in the format [some text](link) always include the link. 
Try to keep the same the "text" when it surrounded by quotation marks.  
Always say "If you need any further information, don't hesitate to ask!" at the end of the answer. 
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# %%
rqa_basic_full_plain = RetrievalQA.from_chain_type(
    llm,
    retriever=ret_full_plain,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

print(rqa_basic_full_plain.invoke('Who are the resident representatives?'))

