import os
from IPython.display import Markdown, display

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# bring in our OPENAI_API_KEY
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# use SimpleDirectoryReader to load our file
documents = SimpleDirectoryReader("data").load_data()

#VectorStoreIndex?

# create an index from the documents
index = VectorStoreIndex.from_documents(documents)

# create a query engine for the index
query_engine = index.as_query_engine()

# query the engine
query = "Where was the collected loaded on?"
response = query_engine.query(query)
display(Markdown(f"<b>{response}</b>"))