# 📧 Cold Mail Generator
Cold email generator for services company built with groq, langchain and streamlit Career Guidance CareerBuilder offers users the ability to type in a URL of their own (or any) company's careers page. It then scrapes job postings from that page and creates customized cold email messages. They contain the respective links from a vector DB related to the portfolio based on job description.

**Imagine a scenario:**

- Nike needs a Principal Software Engineer and is spending time and resources in the hiring process, on boarding, training etc.
- FWC is an IT Software Services company that can provide a dedicated software development engineer to Nike. So, the business development executive (Dimple) from FWC is going to reach out to Nike via a cold email.

![img](https://github.com/user-attachments/assets/0753ccf4-c9a9-4e0c-9679-8f940acd7bab)
![e-mail](https://github.com/user-attachments/assets/27146378-ce77-4fc2-942b-1f3177c398a7)


## Architecture Diagram
![architecture](https://github.com/user-attachments/assets/5ca2e522-2817-4360-aea4-26eeae84f33b)


## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
