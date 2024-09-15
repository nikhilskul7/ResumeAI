# Resume & Job Description Analyzer

This web app analyzes job descriptions and tailors your resume and cover letter. It extracts keywords, identifies missing skills, and generates a customized cover letter.

## 🚀 Features

1. **Upload Resume**: Place your resume (`resume.pdf`) in the working directory.
2. **Analyze JD**: Paste the job description to get:
   - Keywords from the JD
   - Keywords from a master list
   - Keywords sorted by importance
   - Missing keywords from your resume
   - Sponsorship status
   - Generated points based on missing keywords
3. **Generate Cover Letter**: Create and edit a cover letter, then download it as a PDF.
4. **Short Cover Letter**: Generate a brief cover letter for applications.
5. **Ask Any Question**: Get answers to any questions about the job description.
6. 
## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Google Generative AI
- **File Handling**: PyPDF2, Python-docx, ReportLab

  
## 🛠️ Setup

1. Clone the repository:
   ```bash
  git clone https://github.com/nikhilskul7/ResumeAI.git
   ```

2. Install Python, create a virtual environment, and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Place `resume.pdf` in the working directory.

4. Run the app:
   ```bash
   streamlit run ResumeAI.py
   ```

## 📄 License

This project is licensed under the MIT License.
