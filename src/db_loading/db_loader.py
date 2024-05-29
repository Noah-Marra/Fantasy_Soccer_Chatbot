import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import qdrant_client
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.embeddings.gemini import GeminiEmbedding

from dotenv import load_dotenv
from src.db_loading.parser import parser

load_dotenv()
qdrant_client = QdrantClient(
    url= os.getenv('QDRANT_CLUSTER_URL'), 
    api_key= os.getenv('QDRANT_API_KEY'),
)

def db_loader(folder_path, collection_name):
    documents = parser(folder_path)

    Settings.embed_model = GeminiEmbedding(model_name="models/embedding-001", api_key=os.getenv('GOOGLE_API_KEY'), title='fantasy_soccer_csv')

    vector_store = QdrantVectorStore(client=qdrant_client, collection_name=collection_name)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents=documents, storage_context=storage_context, show_progress=True)

    return index

index = db_loader(r"C:\Users\nmarr\OneDrive\Documents\GitHub\RAG_Fantasy_Soccer_Chat\data\csv", "Fantasy_Soccer")


    

    
