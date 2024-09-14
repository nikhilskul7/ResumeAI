import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from io import BytesIO
import subprocess
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import logging

logging.basicConfig(level=logging.DEBUG)
import requests
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


def input_pdf_text_static(file_path):
    with open(file_path, "rb") as file:
        reader = pdf.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def clean_keywords_response(response_text):
    try:
        # print("Received response_text:", response_text)  # Print the entire response_text

        # Parse the JSON-like string
        response_text = response_text.replace("“", '"').replace(
            "”", '"'
        )  # Replace smart quotes with standard quotes
        response_data = json.loads(response_text)  # Convert to dictionary

        # Extract the keywords
        if "Keywords" in response_data:
            keywords_part = response_data["Keywords"].strip().strip('"')
            keywords = [keyword.strip() for keyword in keywords_part.split(",")]
            return ", ".join(keywords) if keywords else "None"
        else:
            return "The 'Keywords' key is missing in the response."
    except json.JSONDecodeError:
        return "Failed to parse JSON response. Ensure the response is valid JSON."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def clean_points_response(response_text):
    try:
        # print("Received response_text:", response_text)  # Print the entire response_text

        # Parse the JSON-like string
        response_text = response_text.replace("“", '"').replace(
            "”", '"'
        )  # Replace smart quotes with standard quotes
        response_data = json.loads(response_text)  # Convert to dictionary

        # Extract the keywords
        if "Points" in response_data:
            keywords_part = response_data["Points"].strip().strip('"')
            keywords = [keyword.strip() for keyword in keywords_part.split(",")]
            return ", ".join(keywords) if keywords else "None"
        else:
            return "The 'Keywords' key is missing in the response."
    except json.JSONDecodeError:
        return "Failed to parse JSON response. Ensure the response is valid JSON."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def create_word_doc(content, filename):
    doc = Document()
    doc.add_heading("Cover Letter", 0)  # Optional heading

    # Add content to the document with proper text wrapping
    p = doc.add_paragraph()
    p.style.font.name = "Helvetica"
    p.style.font.size = Pt(12)

    # Add content to the paragraph
    p.add_run(content)

    # Save the documents
    doc.save(filename)


def create_pdf_from_text(text, title="Cover Letter"):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=52,
        leftMargin=52,
        topMargin=36,
        bottomMargin=18,
        title="Cover Letter Nikhil",
        author="Nikhil Kulkarni",
    )  # Reduced top margin

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(name="Justify", alignment=TA_JUSTIFY, fontSize=12)
    )  # Increased font size
    styles["Title"].fontSize = 18  # Increase title font size

    content = []

    # Add title
    content.append(Paragraph(title, styles["Title"]))
    content.append(Spacer(1, 12))

    # Add content paragraphs
    for para in text.split("\n"):
        if para.strip() == "":
            content.append(Spacer(1, 12))
        else:
            content.append(Paragraph(para, styles["Justify"]))
        content.append(Spacer(1, 6))

    doc.build(content)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
