import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv
load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

def input_pdf_text_static(file_path):
    with open(file_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() 
    return text

def clean_keywords_response(response_text):
    try:
        #print("Received response_text:", response_text)  # Print the entire response_text

        # Parse the JSON-like string
        response_text = response_text.replace('“', '"').replace('”', '"')  # Replace smart quotes with standard quotes
        response_data = json.loads(response_text)  # Convert to dictionary

        # Extract the keywords
        if 'Keywords' in response_data:
            keywords_part = response_data['Keywords'].strip().strip('"')
            keywords = [keyword.strip() for keyword in keywords_part.split(',')]
            return ', '.join(keywords) if keywords else 'None'
        else:
            return "The 'Keywords' key is missing in the response."
    except json.JSONDecodeError:
        return "Failed to parse JSON response. Ensure the response is valid JSON."
    except Exception as e:
        return f"An error occurred: {str(e)}"