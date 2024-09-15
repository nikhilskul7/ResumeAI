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
    promptForSponsorship
)
from utilities import (
    input_pdf_text_static,
    get_gemini_repsonse,
    clean_keywords_response,
    create_pdf_from_text,
    clean_points_response,
)

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
st.markdown("[Overleaf Resume](https://www.overleaf.com/project/64db9dbbb701b20d11a56c23)")
# Job Description Input
jobDescription = st.text_area("Paste the Job Description")

# Buttons for actions
Analyze = st.button("Analyze")


if "cover_letter_content" not in st.session_state:
    st.session_state.cover_letter_content = ""
if "questions" not in st.session_state:
    st.session_state.questions = ""
resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
if Analyze:

    promptToGetAllTheKeyWords = promptToGetAllTheKeyWords.format(jd=jobDescription)
    responseForAllKeywords = get_gemini_repsonse(promptToGetAllTheKeyWords)

    promptToGetKeywordsFromMaster = promptToGetKeywordsFromMaster.format(
        text=master_keywords, jd=jobDescription
    )
    responseFromMasterList = get_gemini_repsonse(promptToGetKeywordsFromMaster)

    # Process response from both sources
    formatted_response_all = clean_keywords_response(responseForAllKeywords)
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
    promptToGenerateRelevantPoints = promptToGenerateRelevantPoints.format(
        keywords=formatted_response_missing + formatted_response_importance
    )
    responseofRelevantPoints = get_gemini_repsonse(promptToGenerateRelevantPoints)
    formatted_response_points = clean_points_response(responseofRelevantPoints)

    promptForSponsorship=promptForSponsorship.format(jd=jobDescription)
    responseForSponsor=get_gemini_repsonse(promptForSponsorship)
    
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
    st.markdown("**Sponsorship Requirement**")
    st.markdown(responseForSponsor)
    st.markdown("**Relevant Points for Resume**")
    st.markdown(formatted_response_points)

generateCoverLetter = st.button("Generate Cover Letter")

if generateCoverLetter:

    resume = input_pdf_text_static(os.getenv("RESUME_PATH"))
    promptsToGenerateCoverLetter = promptsToGenerateCoverLetter.format(
        jd=jobDescription, resume=resume
    )
    responseofCoverLetter = get_gemini_repsonse(promptsToGenerateCoverLetter)

    st.session_state.cover_letter_content = responseofCoverLetter


edited_content_cover_letter = st.text_area(
    "Preview and Edit Your Cover Letter",
    st.session_state.cover_letter_content,
    height=300,
)


if st.button("Save and Download Cover Letter"):
    try:
        pdf_file = create_pdf_from_text(
            edited_content_cover_letter, title="Cover Letter Nikhil"
        )

        st.download_button(
            label="Download Cover Letter as PDF",
            data=pdf_file,
            file_name="Nikhil_Kulkarni_Cover_Letter.pdf",
            mime="application/pdf",
        )

        st.success("Cover letter PDF is ready for download!")
    except Exception as e:
        st.error(f"An error occurred while creating the PDF: {str(e)}")

if st.button("Shorten the cover letter"):

    promptForShorterCoverLetter = promptForShorterCoverLetter.format(
        cover_letter=st.session_state.cover_letter_content,jd=jobDescription
    )
    responseofMessage = get_gemini_repsonse(promptForShorterCoverLetter)

    st.write(responseofMessage)


questions = st.text_area(
    "Any Other Questions Regarding Application",
    st.session_state.questions,
    height=100,
)
st.session_state.questions = questions


if st.button("Answer"):
    if questions:
        question = st.session_state.questions

        promptForAnyQuestion = promptForAnyQuestion.format(
             jd=jobDescription, question=question
        )
        responseofQuestion = get_gemini_repsonse(promptForAnyQuestion)

        st.write(responseofQuestion)
