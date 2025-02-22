import fitz  # PyMuPDF
import pandas as pd
import xmltodict
from fastapi import UploadFile
import io

async def process_file(file: UploadFile):
    content = await file.read()
    file_type = file.filename.split(".")[-1]

    if file_type == "pdf":
        return extract_text_from_pdf(content)
    elif file_type == "xlsx":
        return extract_text_from_excel(content)
    elif file_type == "xml":
        return extract_text_from_xml(content)
    else:
        return "Unsupported file format"

def extract_text_from_pdf(content):
    doc = fitz.open(stream=content, filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text

def extract_text_from_excel(content):
    df = pd.read_excel(io.BytesIO(content))
    return df.to_string()

def extract_text_from_xml(content):
    data_dict = xmltodict.parse(content)
    return str(data_dict)
