from pypdf import PdfReader

import os
import openai

# from chuck import get_text_chunks
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent

# 3rd‑party resource processing
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Chat models
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Vector DB
import faiss


# Extract the text from each page
text = ''
file = "MDS 3.0 QM USER'S MANUAL v12.1.pdf"
OPENAI_API_KEY = ""
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


llm = OpenAI(model_name="gpt-3.5-turbo-0301", temperature=0)

# embeddings
embeddings = OpenAIEmbeddings()
db_path = "qm_manual"

if not os.path.exists(db_path):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()

    # Debug: write each page to a file (optional)
    # for page in pages:
    #     with open(str(page.metadata["page"]), "w") as text_file:
    #         text_file.write(page.page_content)

    db = FAISS.from_documents(pages, embeddings)
    db.save_local(db_path)
else:
    db = FAISS.load_local(db_path, embeddings)


query = (
    "What is Measure: Percent of Residents Who Made Improvements in Function numerator logic?"
)

# Retrieval QA
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

tools = [
    Tool(
        name="CMS Quality Measures Manual",
        func=qa.run,
        description="Useful for answering questions about the CMS Quality Manual. Input should be a fully formed question.",
    ),
]

# Set up a single‑action agent
tool_names = [tool.name for tool in tools]
llm_chain = LLMChain(llm=llm)
agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    stop=["\nObservation:"],
    allowed_tools=tool_names,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)

# Run the query
agent_executor.run(query)
