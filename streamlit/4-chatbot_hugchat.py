# required libraaries
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

### page config
st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

# login
email = os.getenv('HUGCHAT_EMAIL')
passwd = os.getenv('HUGCHAT_PASSWD')

sign = Login(email, passwd)
try:
    cookies = sign.loadCookies() # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.
except:
    cookies = sign.login()
    sign.saveCookies() # 保存cookies至 usercookies/<email>.json

# 创建一个 ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

### sidebar
with st.sidebar:
    st.title('🤗💬 HugChat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by flavorfan)')

### session state
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

### main panel
# st.title('fan chatbot')
# st.write('Hello world!')

#### layout
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

#### User input
# Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()

#### Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    # chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))