import Pypdf2
import openai
import json as js
from datetime import datetime as dt

#function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(len(reader.numPages)):
            page = reader.getPages[page_num]
            text += page.extract_text()
    return text



