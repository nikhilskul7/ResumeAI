promptToGetKeywordsFromMaster = """
Hey, you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday 
with a deep understanding of tech field,software engineering. 
 
Compare the list of master keywords and tell me which keywords are present in the job description.

master_list:{text}
description:{jd}

I want the response in one single string having the structure
{{"Keywords:""}}
"""


promptToGetAllTheKeyWords = """
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
I want the response in one single string having the structure
{{"Keywords:""}}
"""

promptToGetImportanceOfKeywords="""
you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday with a deep understanding of tech field,software engineering. 
You are ranking candidates on the basis of keywords in job description.
Given a list of keywords and job description, rank these keywords based on their importance and how an
ATS or recruiter would rank candidates based on these keywords.
master_list:{text}
description:{jd}

I want the response in one single string having the structure
{{"Keywords:""}}
"""

promptToGetMissingKeyWordsFromResume="""
you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday with a deep understanding of tech field,software engineering. 
You are ranking a candidate based on keywords provided.
Your task as ATS or recruiter is given a list of keywords and resume,
give me list of missing keywords in the resume by comparing resume and keywords list.
keywords:{text}
resume:{resume}
I want the response in one single string having the structure
{{"Keywords:""}}
"""

promptsToGenerateCoverLetter="""
you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday with a deep understanding of tech field,software engineering. 
your task is to create cover letter based on job description and my resume.
description:{jd}
resume:{resume}
Using the job description, my resume and following template create me the best cover letter which is ready to send.
The cover letter should be highly relevant to job description , it should look like I am perfect match. Change the bullet points to match keywords in job description.
I want the response in one single string having the structure and all the variables should be filled.
Ensure that there is no variable which is still a variable without fail.
Here is template-
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


"""

promptToGenerateRelevantPoints="""
you are a skilled or very experience resume creator. 
Your task is to suggest some points for my resume using keywords that I provide.

I want each and every keyword that I give integrated in the bullet points.
These bullet points should make sense for sure so that if I am asked there should be technical way to explain it.
You can also suggest some new points but it should include all the keywords.
I want the keywords in the points that you give me, only provide me with the points that you changed.
I want ALL of the keywords that I give you to be included in the points at any cost.
I REPEAT THIS IS NON NEGOTIABLE THAT I WANT ALL THE KEYWORDS IN THE POINTS EXPLICITLY.
You should  create few  new or fake points too with these keywords.
The format of these  points should be - Action word - method-technologies- result.
here goes list of keywords and resume-
keywords:{keywords}
I want the response in one single string having the structure seperated by commas. I want 7 points.
{{"Points:""}}
"""


promptForShorterCoverLetter="""
you are a skilled or very experience ATS(Application Tracking System) like Lever, Greenhouse or Workday with a deep understanding of tech field,software engineering. 
Your task is to convert this cover letter into message for hiring manager or recruiter.
The message should match what job description wants and the required keywords.
cover_letter={cover_letter}
I want it in format- 
Hi,

I hope you're doing well. I came across the [Position] opening at [Company],
 and I'm really excited about the opportunity to contribute my skills in [briefly mention key expertise].
I have experience in- 
write 3 points from job description which would make me perfect candidate using points from my resume and changing it ( you can write something fake too.)
I would love the chance to discuss how I can add value to your team. Please let me know if we can arrange a time to chat.

Best regards,
I want response in form of single string with proper indentation- 

"""

promptForAnyQuestion="""
You are a software engineer eager to apply to this company.
Answer this question- question={question}.
It should align with (jd={jd}) and highlights relevant experience 

 The answer should be tailored to the role and company, effectively using the necessary keywords to match the job
   requirements and my expertise.
     It should be concise, around 5-6 lines, and directly address the question provided (question={question}) in a way 
     that impresses the recruiter.
     The response should be in form of question and answer. I have provided you with a question.
"""


# Prompt for checking visa sponsorship
promptForSponsorship = """
Analyze this job description for H-1B visa sponsorship information:

Job description: {jd}

1. Check for explicit statements about visa sponsorship.
2. Look for implicit indications (e.g., citizenship requirements).
3. If no clear information, search online resources like h1bgrader or myvisajobs for the company's sponsorship history.
4. Provide a summary with a hyperlink to any relevant information found.

Response format- :
[ Company_Name: Your analysis  in one line with hyperlink (clickable) if applicable]
"""