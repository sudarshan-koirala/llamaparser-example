import os
import nest_asyncio  # noqa: E402
nest_asyncio.apply()

from IPython.display import Markdown, display

# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# set up parser
parser = LlamaParse(
    api_key=llamaparse_api_key,
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['data/gpt4all.pdf'], file_extractor=file_extractor).load_data()
#print(documents)


# create an index from the parsed markdown
index = VectorStoreIndex.from_documents(documents)

# create a query engine for the index
query_engine = index.as_query_engine()

# query the engine
query = "Where was the collected loaded on?"
response = query_engine.query(query)
display(Markdown(f"<b>{response}</b>"))

