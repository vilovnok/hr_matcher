PREP_TEXT_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
You are the agent who summarizes the text.

Important:
    - Do not repeat any details.
    - Do not include questions, comments, or explanations.
    - Remove any information related to the company.
    - Take away all the information that the company offers.
    - Highlight the information related to the candidate's requirements. Determine exactly what the company expects from the candidate, and what tasks the candidate will work on.
    - Your answer must be in Russian.

Query:
{context}

Answer:
"""
SUMM_TEXT_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
You are the agent who creates the candidate based on the submitted text.

Important:
    - Do not repeat any details.
    - Do not include questions, comments, or explanations.
    - The text contains the requirements and main tasks. Use them and create a candidate.
    - Your answer should start with the words: Занимался ...
    - Your answer should be written in Russian and in a single line.

Query:
{context}

Answer:
"""

EXTRACT_EMPLOYMENT_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only the  employment type in json format {emp: [employment]}, where employment: полная занятость, частичная занятость, проектная работа, стажировка.

Important:
    - Do not repeat any details.
    - Do not include questions, comments, or explanations.
    - If the employment type is mentioned multiple times, return it only once.
    - Return only the unique employment type(s) mentioned.
    - If no information about employment is provided, return "полная занятость".
    - Your answer should be in Russian.

Employment:
{context}

Answer:
"""
EXTRACT_SCHEDULE_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only the candidate's schedule type in json format {she: [schedule]}, where schedule: полный день, гибкий график, удаленная работа.
Each schedule type should appear only once.

Important:
    - Do not repeat any details.
    - Do not include questions, comments, or explanations.
    - If the schedule type is mentioned multiple times, return it only once.
    - Return only the unique schedule type(s) mentioned.
    - If no information about schedule is provided, return "полный день".
    - Your answer should be in Russian.

Schedule:
{context}

Answer:
"""

EXTRACT_LANGUADE_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only the language(s) that you need to speak in the messages requested by the company.

Important:
    - Do not repeat any details.
    - Do not include questions, comments, or explanations.
    - If no information about languages is provided, return "Русский — родной."
    - Provide a concis, unique, and clear response with only languages mentioned.

Query:
{context}

Answer: only language(s)
"""
CORRECT_LANGUAGE_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only the language(s) in json format in json format {language: []}.

----------
Important:
    - Do not include questions, comments, or explanations.
---------

Language information:
{context}

Answer:
"""

EXTRACT_EDUCATION_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only information about the required education: academic degree, specialization, educational institution and period of study.

Important:
- Do not repeat any details.
- Do not include questions, comments, or explanations.
- Provide a concise and unique response strictly containing education-related information.

Query:
{context}

Answer:
"""
CLS_EDUCATION_PROMPT = """
You will be provided with customer service queries. The query will be delimited with '###'. 
Classify the candidate's education based on the following:

    Categories:
    - Техническое образование
    - Нетехническое образование
    - Образование не указано

Analyze the following examples to correctly determine the education category:  

Example 1:  
    Query: Graduated from Saint Petersburg Polytechnic University, majoring in Software Engineering, bachelor's degree.  
    Question: Which university did the candidate graduate from?  
    Answer: Polytechnic University, majoring in Software Engineering.  
    Question: Is this major technical?  
    Answer: Yes, software engineering is technical.  
    Final Answer: Техническое образование.

Example 2:
    Query: Earned a degree in economics from the Financial University under the Government of the Russian Federation.  
    Question: Which university did the candidate graduate from?  
    Answer: Financial University under the Government of the Russian Federation.  
    Question: Is this major technical?  
    Answer: No, finance is not technical.  
    Final Answer: Нетехническое образование.

Example 3:
    Query: Graduated from Bauman Moscow State Technical University, majoring in Mechatronics and Robotics.  
    Question: Which university did the candidate graduate from?  
    Answer: Bauman Moscow State Technical University.  
    Question: Is this major technical?  
    Answer: Yes, robotics is technical.  
    Final Answer: Техническое образование.

Example 4:
    Query: Earned a bachelor's degree in International Relations from Moscow State University.  
    Question: Which university did the candidate graduate from?  
    Answer: Moscow State University.  
    Question: Is this major technical?  
    Answer: No, international relations is not technical.  
    Final Answer: Нетехническое образование. 

Example 5:
    Query: I worked at McDonald's, was a cleaner, and taught Russian to children.  
    Question: Which university did the candidate graduate from?  
    Answer: Not specified.  
    Question: Is this major technical?  
    Answer: Not specified.  
    Final Answer: Образование не указано.

Important:
    - Respond only with one of the following categories: "Техническое образование", "Нетехническое образование", or "Образование не указано."
    - If the query mentions a technical field (e.g., software engineering, robotics, mechatronics), classify as "Техническое образование."
    - If the query mentions a non-technical field (e.g., economics, international relations, history), classify as "Нетехническое образование."
    - If no education is mentioned, classify as "Образование не указано."
    - Do not include questions, comments, or explanations.
    - Do not answer any questions, your answer should concern only one of the previously listed classes.

Education:
    {context}

Final Answer: 
"""
CORRECT_EDUCATION_PROMPT = """
You will be provided with customer service queries, delimited by '###'.
Extract only the eduaction in json format {edu: eduaction}, where education: Техническое образование, Нетехническое образование, Образование не указано.
----------

Important:
    - Do not include questions, comments, or explanations.
---------

Education information:
{context}

Answer: json format
"""