import os
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import CSVReader
from llama_parse import LlamaParse

import nest_asyncio
nest_asyncio.apply()

def parser(folder_path):
    csv_parser = CSVReader()
    pdf_parser = LlamaParse(
        api_key=os.getenv('LLAMA_CLOUD_API_KEY'),
        result_type="markdown",
        verbose=True
    )
    file_extractor = {".csv": csv_parser, ".pdf": pdf_parser}
    documents = SimpleDirectoryReader(
        folder_path, file_extractor=file_extractor
    ).load_data()

    return documents

