# %%
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

from langchain.evaluation.loading import load_dataset
dataset = load_dataset("llm-math")
# %%
len(dataset)
# %%
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
llm = OpenAI()
chain = LLMMathChain(llm=llm)
predictions = chain.apply(dataset[:1])
# %%
print(predictions)