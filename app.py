import streamlit as st
import os
from dotenv import load_dotenv
from master_list import master_keywords
from prompts import (
    promptToGetKeywordsFromMaster,
    promptToGetAllTheKeyWords,
    promptToGetImportanceOfKeywords,
    promptToGetMissingKeyWordsFromResume,
    promptsToGenerateCoverLetter,
)
from utilities import (
    input_pdf_text_static,
    get_gemini_repsonse,
    clean_keywords_response,
create_pdf_from_text
)

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

# Job Description Input
jobDescription = st.text_area("Paste the Job Description")

# Buttons for actions
Analyze = st.button("Analyze")
generateCoverLetter = st.button("Generate Cover Letter")


if 'cover_letter_content' not in st.session_state:
    st.session_state.cover_letter_content = ""

if Analyze:
    resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
    promptToGetAllTheKeyWords = promptToGetAllTheKeyWords.format(jd=jobDescription)
    response = get_gemini_repsonse(promptToGetAllTheKeyWords)
    promptToGetKeywordsFromMaster = promptToGetKeywordsFromMaster.format(
        text=master_keywords, jd=jobDescription
    )
    responseFromMasterList = get_gemini_repsonse(promptToGetKeywordsFromMaster)

    # Process response from both sources
    formatted_response_all = clean_keywords_response(response)
    formatted_response_master = clean_keywords_response(responseFromMasterList)

    promptToGetImportanceOfKeywords = promptToGetImportanceOfKeywords.format(
        text=(formatted_response_all + formatted_response_master), jd=jobDescription
    )
    responseFromImportance = get_gemini_repsonse(promptToGetImportanceOfKeywords)
    formatted_response_importance = clean_keywords_response(responseFromImportance)

    promptToGetMissingKeyWordsFromResume = promptToGetMissingKeyWordsFromResume.format(
        text=formatted_response_importance, resume=resume
    )
    responseofMissingKeywordsFromResume = get_gemini_repsonse(
        promptToGetMissingKeyWordsFromResume
    )
    formatted_response_missing = clean_keywords_response(
        responseofMissingKeywordsFromResume
    )

    # Display analysis results
    st.subheader("ATS Keywords Analysis Result")
    st.markdown("**All Possible Keywords**")
    st.markdown(formatted_response_all)
    st.markdown("**Keywords from master list**")
    st.markdown(formatted_response_master)
    st.markdown("**Important Keywords**")
    st.markdown(formatted_response_importance)
    st.markdown("**Missing Keywords From Resume**")
    st.markdown(formatted_response_missing)


if generateCoverLetter:

    resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
    promptsToGenerateCoverLetter = promptsToGenerateCoverLetter.format(
        jd=jobDescription, resume=resume
    )
    responseofCoverLetter = get_gemini_repsonse(promptsToGenerateCoverLetter)
    
    
    # Editable text area
    st.session_state.cover_letter_content = responseofCoverLetter

edited_content = st.text_area("Preview and Edit Your Cover Letter", st.session_state.cover_letter_content, height=300)

if st.button("Save and Download Cover Letter"):
    try:
        pdf_file = create_pdf_from_text(edited_content)
        
        st.download_button(
            label="Download Cover Letter as PDF",
            data=pdf_file,
            file_name="Nikhil_Kulkarni_Cover_Letter.pdf",
            mime="application/pdf",
        )
        
        st.success("Cover letter PDF is ready for download!")
    except Exception as e:
        st.error(f"An error occurred while creating the PDF: {str(e)}")