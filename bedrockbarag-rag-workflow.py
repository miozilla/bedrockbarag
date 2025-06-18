from langchain.chains import RetrievalQA
from langchain.llms import BedrockLLM
from langchain.vectorstores import OpenSearchVectorSearch

retriever = OpenSearchVectorSearch(...)
llm = BedrockLLM(model_id='amazon.titan-text-lite-v1')

qa_chain = RetrievalQA(llm=llm, retriever=retriever)
response = qa_chain.run("What are our Q2 revenue highlights?")