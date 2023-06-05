# %%
from langchain.vectorstores import FAISS


# create vectory db
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
loader = TextLoader('../../../state_of_the_union.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()


db = FAISS.from_documents(docs, embeddings)

# querry by db function : similarity_search
query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)
print(docs[0].page_content)


# similarity_search_with_score
docs_and_scores = db.similarity_search_with_score(query)
docs_and_scores[0]


############ query in chain
# llm = ChatOpenAI()
# llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
# memory = ConversationBufferMemory(
#     memory_key='chat_history', return_messages=True)
# conversation_chain = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=vectorstore.as_retriever(),
#     memory=memory
# )
# response = st.session_state.conversation({'question': user_question})

# saving and loading
db.save_local("faiss_index")

new_db = FAISS.load_local("faiss_index", embeddings)
docs = new_db.similarity_search(query)


# merging
db1 = FAISS.from_texts(["foo"], embeddings)
db2 = FAISS.from_texts(["bar"], embeddings)

db1.docstore._dict
db2.docstore._dict


db1.merge_from(db2)
db1.docstore._dict


