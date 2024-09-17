import streamlit as st
import os
from ats_functions import (
    analyze_job_description,
    generate_resume,
    generate_cover_letter,
    save_cover_letter,
    shorten_cover_letter,
    answer_question,
)
from utilities import load_latex_code

# Streamlit app
st.set_page_config(layout="wide", page_title="Smart ATS")

def main():
    st.title("Smart ATS")
    st.subheader("Improve Your Resume ATS")
    
    # Job Description Section
    st.header("1. Job Description Analysis")
    jobDescription = st.text_area("Paste the Job Description", height=200)
    if st.button("Analyze Job Description"):
        analyze_job_description(jobDescription)
    
    if 'analysis_complete' in st.session_state and st.session_state.analysis_complete:
        display_analysis_results()
    
    # Resume Section
    st.header("2. Resume Editor")
    display_resume_editor()
    
    # Cover Letter Section
    st.header("3. Cover Letter Generator")
    display_cover_letter_section()
    
    # Questions Section
    st.header("4. Additional Questions")
    display_question_section()

def display_analysis_results():
    st.subheader("ATS Keywords Analysis Result")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**All Possible Keywords**")
        st.markdown(st.session_state.formatted_response_all)
        st.markdown("**Important Keywords**")
        st.markdown(st.session_state.formatted_response_importance)
        st.markdown("**Sponsorship Requirement**")
        st.markdown(st.session_state.responseForSponsor)
    
    with col2:
        st.markdown("**Keywords from Master List**")
        st.markdown(st.session_state.formatted_response_master)
        st.markdown("**Missing Keywords From Resume**")
        st.markdown(st.session_state.formatted_response_missing)
        st.markdown("**Relevant Points for Resume**")
        st.markdown(st.session_state.formatted_response_points)

def display_resume_editor():
    st.markdown("[Overleaf Resume](https://www.overleaf.com/project/64db9dbbb701b20d11a56c23)")
    
    latex_files = {
        'General Resume': os.getenv("LATEX_RESUME_GENERAL"),
        '.NET Resume': os.getenv("LATEX_RESUME_NET"),
        'Frontend Resume': os.getenv("LATEX_RESUME_FRONTEND"),
        'Node Backend Resume': os.getenv("LATEX_RESUME_NODE"),
        'Java Backend Resume': os.getenv("LATEX_RESUME_JAVA"),
        'DevOps Backend Resume': os.getenv("LATEX_RESUME_DEVOPS"),
    }
    selected_resume = st.selectbox('Select Resume to Edit:', options=list(latex_files.keys()))
    
    latex_resume_path = latex_files[selected_resume]
    latex_code = load_latex_code(latex_resume_path)
    edited_code = st.text_area("Edit your resume", latex_code, height=300)
    
    if st.button("Generate Resume"):
        generate_resume(edited_code)

def display_cover_letter_section():
    if st.button("Generate Cover Letter"):
        generate_cover_letter()
    
    if 'cover_letter_content' in st.session_state:
        edited_content_cover_letter = st.text_area(
            "Preview and Edit Your Cover Letter",
            st.session_state.cover_letter_content,
            height=300,
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save and Download Cover Letter"):
                save_cover_letter(edited_content_cover_letter)
        
        with col2:
            if st.button("Shorten the cover letter"):
                shorten_cover_letter()

def display_question_section():
    question = st.text_area("Any Other Questions Regarding Application", height=100)
    
    if st.button("Answer"):
        if question:
            answer_question(question)

if __name__ == "__main__":
    main()