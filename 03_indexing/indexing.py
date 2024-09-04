from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings()

# CONNECTION_STRING = os.environ.get("POSTGRES_CONNECTION_STRING")
# COLLECTION_NAME = "vectordb"

loader = DirectoryLoader("./data", glob="**/*.txt")
docs = loader.load()
# print(f"{len(docs)} documents loaded!")
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=20,
#     length_function=len,
#     is_separator_regex=False,
# )
# chunks = text_splitter.split_documents(docs)
# print(f"{len(chunks)} chunks from {len(docs)} docs created!")

# vectorstore = PGVector(
#     connection_string=CONNECTION_STRING,
#     embedding_function=embeddings,
#     collection_name=COLLECTION_NAME,
# )
#
# vectorstore.add_documents(chunks)