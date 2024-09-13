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