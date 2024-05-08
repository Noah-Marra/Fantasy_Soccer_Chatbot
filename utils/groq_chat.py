import os
from llama_index.llms.groq import Groq

groq_key = os.getenv("GROQ_API_KEY")

def groq_chat():
    
    llm = Groq(model = "llama3-70b-8192", api_key = groq_key)