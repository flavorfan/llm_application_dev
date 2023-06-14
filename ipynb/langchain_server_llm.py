import os

# os.environ["OPENAI_API_KEY"] = "xxx"
# os.environ['LANGCHAIN_HANDLER'] = "langchain"
# os.environ['LANGCHAIN_SESSION'] = "mysession"

# os.environ['HTTP_PROXY']='xxx'
# os.environ['HTTPS_PROXY']='xxx'
# os.environ['no_proxy']="localhost,127.0.0.1,localaddress,localdomain.com"

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from langchain.agents import initialize_agent, Tool, load_tools
from langchain.agents import AgentType

tools = load_tools(['llm-math'], llm=OpenAI(temperature=0))

agent = initialize_agent(tools, OpenAI(temperature=0), 
                        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                        verbose=True)

output = agent.run("What is 5+58?")

print(output)
