### required libraaries
import os
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

# from hugchat import hugchat
# from hugchat.login import Login
# langchai
from langchain.llms import OpenAI



from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# st.title('🦜🔗 Quickstart App')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')
# llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
llm = OpenAI(temperature=0.7)


def generate_response(input_text):  
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
#   if not openai_api_key.startswith('sk-'):
#     st.warning('Please enter your OpenAI API key!', icon='⚠')
#   if submitted and openai_api_key.startswith('sk-'):
  if submitted:
    generate_response(text)