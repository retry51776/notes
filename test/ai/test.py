from pypdf import PdfReader

import os
import openai

#from chuck import get_text_chunks
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent

# 3rd party resource process
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# chat models
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

# Vector DB
import faiss


# Extract the text from each page
text = ''
file = "MDS 3.0 QM USER'S MANUAL v12.1.pdf"
OPENAI_API_KEY=""
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


llm = OpenAI(model_name='gpt-3.5-turbo-0301', temperature=0)

#print(llm('What is the meaning of life?'))

# Embedding Process
embeddings = OpenAIEmbeddings()
db_path = "qm_manual"
if not os.path.exists(db_path):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()

    # Debug
    # for page in pages:
    #     with open(str(page.metadata["page"]), 'w') as text_file:
    #         text_file.write(page.page_content)

    db = FAISS.from_documents(pages, embeddings)
    db.save_local(db_path)
else:
    db = FAISS.load_local(db_path, embeddings)


# system_template = """
# context: {context}
# history: {history}
# """

# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
#     SystemMessagePromptTemplate,
# )
# messages = [
#     SystemMessagePromptTemplate.from_template(system_template),
#     HumanMessagePromptTemplate.from_template("{question}"),
# ]

# prompt = ChatPromptTemplate.from_messages(messages)
# history = []
# while True:
#     query = input("Enter a question: ")
#     resp = xxx
#     history.append(query)

query = "What is Measure: Percent of Residents Who Made Improvements in Function numerator logic?"

# from langchain.chains.question_answering import load_qa_chain
# from langchain.chains.qa_with_sources import load_qa_with_sources_chain
# qa = load_qa_chain(llm=llm)
# docs = db.similarity_search(query, k=3)
# resp = qa.run(input_documents=docs, question=query)
# print('resp', resp)


from langchain.chains import RetrievalQAWithSourcesChain, RetrievalQA
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
# resp = qa({
#     "question": "What is Measure: Percent of Residents Who Made Improvements in Function numerator logic?",
# })
# print('resp', resp)


from langchain.agents import initialize_agent, Tool
tools = [
    Tool(
        name = "CMS Quality Measures Manual",
        func=qa.run,
        description="useful for when you need to answer questions about CMS Quality Manual. Input should be a fully formed question."
    ),
]

#agent = initialize_agent(tools, llm=llm, agent="zero-shot-react-description", verbose=True)
#agent.run(query)

# tools = load_tools(['wikipedia'], llm=llm)
# agent.run("Who is 34th president of the United States?")

from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain import SerpAPIWrapper, LLMChain
llm_chain = LLMChain(llm=llm)
tool_names = [tool.name for tool in tools]
agent = LLMSingleActionAgent(
    llm_chain=llm_chain, 
    stop=["\nObservation:"], 
    allowed_tools=tool_names
)
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

agent_executor.run(query)


# resp = llm([
#     SystemMessage(content="You will play the role of a human therapist name Luce who treat me as a mental health patient. Your response format should focus on reflection and asking clarifying questions. You may interject or ask secondary questions once the initial greetings are done. Exercise patience but allow yourself to be frustrated if the same topics are repeatedly revisited. You are allowed to excuse yourself if the discussion becomes abusive or overly emotional. Begin by welcoming me to your office and asking me for my name. Wait for my response. Then ask how you can help. Do not break character. Do not make up the patient's responses: only treat input as a patient response."),
#     HumanMessage(content="My name is Terry, I am bad at agree with people."),
# ])
# print(resp)
# standard text process
# pdf_reader = PdfReader(file)
# for page in pdf_reader.pages:
#     text += page.extract_text()

# # Print the extracted text
# new_file_name = file.replace('.pdf', '.txt')
# with open(new_file_name, 'w') as text_file:
#     text_file.write(text)

# chucks = get_text_chunks(text, 4000)

# for idx, chuck in enumerate(chucks):
#     chuck_name = f"{idx}.txt"
#     with open(chuck_name, 'w') as chunk_file:
#         chunk_file.write(chuck)
