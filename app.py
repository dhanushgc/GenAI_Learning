from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name='gpt-3.5-turbo',temperature=0.6)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("LangChain Application")
submit=st.button("Ask AI") 

input = st.text_input("Input:", key="input")
response = get_openai_response(input)


if submit:
    st.subheader("The Response is")
    st.write(response)
