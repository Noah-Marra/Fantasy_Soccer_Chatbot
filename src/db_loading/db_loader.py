import os
from qdrant_client import QdrantClient
from src.db_loading.parser import csv_parser, pdf_parser


qdrant_client = QdrantClient(
    url= os.getenv('QDRANT_CLUSTER_URL'), 
    api_key= os.getenv('QDRANT_API_KEY'),
)

def db_loader(csv_folder_path, pdf_folder_path):
    csv_documents = csv_parser(csv_folder_path)
    pdf_documents = pdf_parser(csv_folder_path)
