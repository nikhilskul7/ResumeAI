# Prompt to extract keywords from master list
promptToGetKeywordsFromMaster = """
As an advanced ATS with expertise in tech and software engineering, compare the master keyword list to the job description.
Identify which keywords are present in the description.

Master list: {text}
Job description: {jd}

I want the response in one single string having the structure
{{"Keywords:""}}
"""

# Prompt to extract all keywords from job description
promptToGetAllTheKeyWords = """
As an advanced ATS specializing in tech and software engineering, extract all relevant keywords from this job description that might be used to rank resumes.
 Focus on hard skills and technical terms, sorted by importance.

Job description: {jd}

I want the response in one single string having the structure
{{"Keywords:""}}
"""

# Prompt to rank keywords by importance
promptToGetImportanceOfKeywords = """
As an ATS expert in tech and software engineering, rank these keywords based on their 
importance for candidate evaluation, considering the job description.

Keywords: {text}
Job description: {jd}

I want the response in one single string having the structure
{{"Keywords:""}}
"""

# Prompt to identify missing keywords in resume
promptToGetMissingKeyWordsFromResume = """
As an ATS specialist in tech and software engineering,
 compare the given keywords to the resume and list the missing keywords.

Keywords: {text}
Resume: {resume}

I want the response in one single string having the structure
{{"Keywords:""}}
"""

# Prompt to generate a cover letter
promptsToGenerateCoverLetter = """
Create a tailored cover letter based on the job description and resume. 
Ensure it highlights relevant experience and aligns closely with the job requirements.
DO NOT MAKE IT LOOK LIKE AN LLM DID THIS .
Job description: {jd}
Resume: {resume}

Use this template, filling in all variables:
Nikhil Kulkarni,
[Role],
[Location]

To,
Hiring Manager,
[Company Name],
[Location],
[Date],

Subject: Cover Letter for [Position] Role at [Company]

Dear Hiring Manager,

I am writing to express my interest in the [Position] role at [Company Name]. With a Master’s degree in Computer Science, hands-on experience in full-stack development, and a passion for delivering innovative solutions, I am excited about the opportunity to contribute to [Company Name]'s mission and vision.

A bit about my experience ( match them perfectly with job desctiption and it's keywords):

- write 3 points from job description which would make me perfect candidate using points from my resume and changing it ( you can write something fake too.).
- Change the technologies I have in my resume to match the job description. Make those technical points and have the same keywords from job description.
- make me look like the perfect candidate. Always write 3 bullet points and point template from the resume. You can fake details about my resume

I am particularly excited about the prospect of joining [Company Name] due to [specific area or value you admire]. Your commitment to [specific industry or mission] really resonates with me, and I am eager to contribute to such a forward-thinking team.

Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experience align with the goals of your team.
Please let me know if there’s any additional information I can provide. You can reach me at [Email Address].

Best regards,

Nikhil Kulkarni
[LinkedIn Profile: https://www.linkedin.com/in/nikhil-kulkarni-nk/]
[Personal Portfolio: https://portfolio-one-gamma-30.vercel.app/]

Response format:
[Completed cover letter]
"""

# Prompt to generate relevant resume points
promptToGenerateRelevantPoints = """
Create 7 resume bullet points that incorporate all provided keywords. 
Each point should follow the format: Action word - method - technologies - result. 
Include some new or enhanced points to fully utilize all keywords.
DO NOT MAKE IT LOOK LIKE AN LLM DID THIS .
Keywords: {keywords}

I want the response in one single string having the structure, I want points seperated by | and no " in them.
{{"Points:"}}
"""

# Prompt for shorter cover letter
promptForShorterCoverLetter = """
Convert this cover letter into a concise message for the hiring manager, highlighting key skills that match the job requirements.
The message should match what job description wants and the required keywords.
jd={jd}
Cover letter: {cover_letter}
DO NOT MAKE IT LOOK LIKE AN LLM DID THIS .
I want it in format- 
Hi [Hiring Manager's Name],

I hope you're doing well. I came across the [Position] opening at [Company],
 and I'm really excited about the opportunity to contribute my skills in [briefly mention key expertise].
I have experience in- 
write 3 points from job description which would make me perfect candidate using points from my resume and changing it ( you can write something fake too.)
I would love the chance to discuss how I can add value to your team. Please let me know if we can arrange a time to chat.

Best regards,
I want response in form of single string with proper indentation- 
"""

# Prompt for answering interview questions
promptForAnyQuestion = """
Answer this interview question as a software engineer applying to the company. 
Align your response with the job description.
DO NOT MAKE IT LOOK LIKE AN LLM DID THIS .
Question: {question}
Job description: {jd}


Provide a concise 5-6 line response that impresses the recruiter.

Response format:
Q: [Question]
A: [Your tailored answer]
"""

# Prompt for checking visa sponsorship
promptForSponsorship = """
Analyze this job description for H-1B visa sponsorship information:

Job description: {jd}

1. Check for explicit statements about visa sponsorship.
2. Look for implicit indications (e.g., citizenship requirements).
3. If no clear information, search online resources like h1bgrader or myvisajobs for the company's sponsorship history.
4. Provide a summary with a hyperlink to any relevant information found.

Response format:
[Your analysis  in one line with hyperlink if applicable]
"""