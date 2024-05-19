from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import CSVReader
from llama_parse import LlamaParse

import nest_asyncio
nest_asyncio.apply()

def csv_parser(folder_path):
    parser = CSVReader()
    file_extractor = {".csv": parser}  # Add other CSV formats as needed
    documents = SimpleDirectoryReader(
        folder_path, file_extractor=file_extractor
    ).load_data()

    return documents

def pdf_parser(folder_path):
    documents = LlamaParse(
        result_type="markdown"
    ).load_data(folder_path)

    return documents

