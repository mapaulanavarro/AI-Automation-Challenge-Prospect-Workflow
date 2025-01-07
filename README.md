# AI-Automation-Challenge-Prospect-Workflow

Candidate: Maria Paula Navarro 

Your task is to create an AI-powered workflow that automates prospect company research for a sales team. The workflow should take a company website as input and produce a concise, informative article about this prospect for the sales team as output. 
We'd like you to create a basic working version of your workflow using any tool you're comfortable with (AirOps, Clay, n8n, Zapier, Retool, Gumloop, Python, JavaScript, or any other tool of your choice). 

Please, send a link with the result of your workflow, and describe the reasoning for your approach.


Input: A company website URL
Output: A concise, informative article about the company

Steps:
1. Extract key information from the company's website.
2. Summarize the extracted information.
3. Generate a resume for evaluation or data analysis.

The Tools and Libraries used are Python for coding, 
- Python: For coding the workflow.
- Selenium for web scraping.
- Ollama Ai: To generate the summary.

For this project, I developed a Streamlit web interface that allows users to input a company URL. The system leverages Selenium for dynamic web scraping, extracting relevant company information directly from the website. 
Additionally, I integrated LangChain to interact with the Ollama AI model, enabling it to generate prompts and retrieve the specific insights requested. This combination creates a seamless workflow for automated company research and analysis.

This code work for the Chrome version 131.0.6779.204

This code only work if you have Ollama version3 installed.






