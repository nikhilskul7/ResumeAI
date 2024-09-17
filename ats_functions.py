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
    promptToGenerateRelevantPoints,
    promptForShorterCoverLetter,
    promptForAnyQuestion,
    promptForSponsorship,
)
from utilities import (
    input_pdf_text_static,
    get_gemini_repsonse,
    clean_keywords_response,
    create_pdf_from_text,
    clean_points_response,
    load_latex_code,
    save_latex_code,
    latex_to_pdf,
    extract_company_name,
)

# Load environment variables
load_dotenv()

def analyze_job_description(jobDescription):
    with st.spinner("Analyzing job description..."):
        formatted_prompt_all_keywords = promptToGetAllTheKeyWords.format(jd=jobDescription)
        responseForAllKeywords = get_gemini_repsonse(formatted_prompt_all_keywords)

        formatted_prompt_master_keywords = promptToGetKeywordsFromMaster.format(
            text=master_keywords, jd=jobDescription
        )
        responseFromMasterList = get_gemini_repsonse(formatted_prompt_master_keywords)

        formatted_response_all = clean_keywords_response(responseForAllKeywords)
        formatted_response_master = clean_keywords_response(responseFromMasterList)

        formatted_prompt_importance = promptToGetImportanceOfKeywords.format(
            text=(formatted_response_all + formatted_response_master), jd=jobDescription
        )
        responseFromImportance = get_gemini_repsonse(formatted_prompt_importance)
        formatted_response_importance = clean_keywords_response(responseFromImportance)

        resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
        formatted_prompt_missing_keywords = promptToGetMissingKeyWordsFromResume.format(
            text=formatted_response_importance, resume=resume
        )
        responseofMissingKeywordsFromResume = get_gemini_repsonse(
            formatted_prompt_missing_keywords
        )
        formatted_response_missing = clean_keywords_response(
            responseofMissingKeywordsFromResume
        )

        formatted_prompt_relevant_points = promptToGenerateRelevantPoints.format(
            keywords=formatted_response_missing + formatted_response_importance
        )
        responseofRelevantPoints = get_gemini_repsonse(formatted_prompt_relevant_points)
        formatted_response_points = clean_points_response(responseofRelevantPoints)

        formatted_prompt_sponsorship = promptForSponsorship.format(jd=jobDescription)
        responseForSponsor = get_gemini_repsonse(formatted_prompt_sponsorship)
        
        st.session_state.jobDescription = jobDescription
        st.session_state.analysis_complete = True
        st.session_state.formatted_response_all = formatted_response_all
        st.session_state.formatted_response_master = formatted_response_master
        st.session_state.formatted_response_importance = formatted_response_importance
        st.session_state.formatted_response_missing = formatted_response_missing
        st.session_state.responseForSponsor = responseForSponsor
        st.session_state.formatted_response_points = formatted_response_points
        st.session_state.company = extract_company_name(responseForSponsor)
    
    st.success("Analysis complete!")
    st.rerun()

def generate_resume(edited_code):
    with st.spinner("Generating resume..."):
        latex_code_file_name = f"Nikhil_Kulkarni_Resume_{st.session_state.company}.tex"
        save_path = os.path.join("resumes", latex_code_file_name)
        save_latex_code(save_path, edited_code)
        latex_to_pdf(save_path, "resumes/")
    st.success("Resume PDF downloaded in resumes folder!")

def generate_cover_letter():
    with st.spinner("Generating cover letter..."):
        resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
        formatted_prompt_cover_letter = promptsToGenerateCoverLetter.format(
            jd=st.session_state.jobDescription, resume=resume
        )
        responseofCoverLetter = get_gemini_repsonse(formatted_prompt_cover_letter)
        st.session_state.cover_letter_content = responseofCoverLetter
    st.success("Cover letter generated!")
    st.rerun()

def save_cover_letter(content):
    try:
        pdf_filename = f"Nikhil_Kulkarni_Cover_Letter_{st.session_state.company}.pdf"
        save_path = os.path.join("cover_letters", pdf_filename)
        pdf_file = create_pdf_from_text(content, title="Cover Letter")
        with open(save_path, "wb") as f:
            f.write(pdf_file)
        st.success("Cover letter PDF downloaded in cover letter folder!")
    except Exception as e:
        st.error(f"An error occurred while creating the PDF: {str(e)}")

def shorten_cover_letter():
    with st.spinner("Shortening cover letter..."):
        formatted_prompt_shorter_cover_letter = promptForShorterCoverLetter.format(
            cover_letter=st.session_state.cover_letter_content, 
            jd=st.session_state.jobDescription
        )
        responseofMessage = get_gemini_repsonse(formatted_prompt_shorter_cover_letter)
        st.session_state.cover_letter_content = responseofMessage
    st.success("Cover letter shortened!")
    st.rerun()

def answer_question(question):
    with st.spinner("Generating answer..."):
        formatted_prompt_any_question = promptForAnyQuestion.format(
            jd=st.session_state.jobDescription, question=question
        )
        responseofQuestion = get_gemini_repsonse(formatted_prompt_any_question)
        st.write(responseofQuestion)