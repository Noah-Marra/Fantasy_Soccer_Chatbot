import os
from llama_index.llms.groq import Groq

groq_key = os.getenv("GROQ_API_KEY")

llm = Groq(model = "llama3-70b-8192", api_key = groq_key)

#TODO: add support for ingesting the qdrant database using: index = VectorStoreIndex.from_vector_store(
#     vector_store=vector_store, service_context=service_context
# )