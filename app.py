import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import openai
load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # or "gpt-4" if you prefer the latest model
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    return response.choices[0].text.strip()

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

# Define the static path to your PDF file
static_pdf_file_path = "resume.pdf"
#Prompt Template

input_prompt="""
Hey, you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday 
with a deep understanding of tech field,software engineering. 
 
The list of missing keywords should be what the ATS may use to rank this resume higher and be hard skills.


Your task is to evaluate given resume based on the given job description.

resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"Job description match":"%","MissingKeywords:[]""}}
"""


input_prompt2="""
you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday with a deep understanding of tech field,software engineering. 
I need to identify the keywords from the following job description that an Applicant Tracking System (ATS) 
might use to rank resumes. 
Please extract and list all relevant keywords and phrases that are likely to be important for the ATS.
The list of missing keywords should be what the ATS may use to rank this resume higher and be hard skills and technical.

Here is the job description:
job description:{jd}
I want the response in one single string having the structure and keywords should be seperated by commas.
sort them in order of their importance.
The keywords should be from job description.
{{"Keywords:""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
#uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

GetKeywords = st.button("Get Keywords")
GetMissingKeywords = st.button("Get Missing Keywords")

if GetKeywords:
    
        #text=input_pdf_text(uploaded_file)
        text=input_pdf_text_static(static_pdf_file_path)
        response=get_chatgpt_response(input_prompt2)
        print(response)
        try:
            cleaned_response = response.replace('{{', '').replace('}}', '').strip()
    
            # Extract keywords part (assumes "Keywords:" is the start of the relevant part)
            if cleaned_response.startswith('"Keywords:'):
                keywords_part = cleaned_response[len('"Keywords:'):].strip(' "')
            else:
                raise ValueError("Response format is unexpected")

            # Split keywords by comma and strip any extra whitespace
            keywords = [keyword.strip() for keyword in keywords_part.split(',')]

            # Create a formatted response string
            formatted_response = (
                f"**Keywords:** {', '.join(keywords) if keywords else 'None'}"
            )
        except json.JSONDecodeError:
            formatted_response = "Failed to parse response from the API. Ensure the API returns valid JSON."
        except Exception as e:
            formatted_response = f"An error occurred: {str(e)}"
        # Display the formatted response in Streamlit
        st.subheader("ATS Keywords Analysis Result")
        st.markdown(formatted_response)

if GetMissingKeywords:
    text=input_pdf_text_static(static_pdf_file_path)
    response=get_gemini_repsonse(input_prompt)
    try:
            cleaned_response = response.replace("{{", "{").replace("}}", "}").replace('“', '"').replace('”', '"')

            # Load the cleaned response as JSON
            response_json = json.loads(cleaned_response)

            # Extract information from the JSON
            jd_match = response_json.get("Job description match", "N/A")
            missing_keywords = response_json.get("MissingKeywords", [])

            # Create a formatted response string
            formatted_response = (
                f"**Job Description Match:** {jd_match}\n\n"
                f"**Missing Keywords:** {', '.join(missing_keywords) if missing_keywords else 'None'}"
            )
    except json.JSONDecodeError:
            formatted_response = "Failed to parse response from the API. Ensure the API returns valid JSON."
    except Exception as e:
            formatted_response = f"An error occurred: {str(e)}"
        # Display the formatted response in Streamlit
    st.subheader("ATS Analysis Result")
    st.markdown(formatted_response)