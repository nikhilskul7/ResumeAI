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
