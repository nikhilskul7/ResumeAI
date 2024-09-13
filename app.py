import streamlit as st


import json
from master_list import master_keywords
from prompts import input_prompt,input_prompt2
from utilities import input_pdf_text_static,get_gemini_repsonse

# Define the static path to your PDF file
static_pdf_file_path = "resume.pdf"

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")

GetKeywords = st.button("Get Keywords")
GetMissingKeywords = st.button("Get Missing Keywords")

if GetKeywords:
    
        #text=input_pdf_text(uploaded_file)
        text=input_pdf_text_static(static_pdf_file_path)
        response=get_gemini_repsonse(input_prompt2)

        try:
            cleaned_response = response.replace('{{', '').replace('}}', '').strip()

            if cleaned_response.startswith('"Keywords:'):
                keywords_part = cleaned_response[len('"Keywords:'):].strip(' "')
            else:
                raise ValueError("Response format is unexpected")

            keywords = [keyword.strip() for keyword in keywords_part.split(',')]

            formatted_response = (
                f"**Keywords:** {', '.join(keywords) if keywords else 'None'}"
            )
        except json.JSONDecodeError:
            formatted_response = "Failed to parse response from the API. Ensure the API returns valid JSON."
        except Exception as e:
            formatted_response = f"An error occurred: {str(e)}"

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