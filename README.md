# AI-Automation-Challenge-Prospect-Workflow

### Candidate: Maria Paula Navarro 

Your task is to create an AI-powered workflow that automates prospect company research for a sales team. The workflow should take a company website as input and produce a concise, informative article about this prospect for the sales team as output. 
We'd like you to create a basic working version of your workflow using any tool you're comfortable with (AirOps, Clay, n8n, Zapier, Retool, Gumloop, Python, JavaScript, or any other tool of your choice). 

Please, send a link with the result of your workflow, and describe the reasoning for your approach.

**Steps:** 
1. Extract key information from the company's website.
2. Summarize the extracted information.
3. Generate a resume for evaluation or data analysis.

**The Tools and Libraries used are:**
- Python: For coding the workflow.
- Selenium for web scraping.
- Ollama Ai: To generate the summary.

Additional info to keep in mind:

- Input: A company website URL

- Output: A concise, informative article about the company

For this project, I developed a Streamlit web interface that allows users to input a company URL. The system leverages Selenium for dynamic web scraping, extracting relevant company information directly from the website. 
Additionally, I integrated LangChain to interact with the Ollama AI model, enabling it to generate prompts and retrieve the specific insights requested. This combination creates a seamless workflow for automated company research and analysis.

This code work for the Chrome version 131.0.6779.204

This code only work if you have Ollama version3 installed.

The reasoning behind this approach lies in creating an efficient, user-friendly, and dynamic system for automated company research. 
1. Ease of Use: Streamlit provides a simple and interactive interface for users to input a company URL, making the tool accessible to non-technical users like sales teams.
2. Rapid Prototyping: Streamlit allows for quick deployment and iterative improvements, ideal for testing and scaling.
3. Selenium, being a browser automation tool, can navigate and scrape such websites effectively, ensuring accurate data extraction.
4. Versatility: Selenium can handle interactive elements (e.g., drop-down menus or pop-ups), making it more robust than static scraping libraries like Beautiful Soup.
5. LangChain for AI Prompting: LangChain enables seamless interaction with AI models by building chains of prompts and logic, making it easier to tailor responses for specific use cases.
6. Scalability: LangChain supports integration with multiple AI models and APIs, providing flexibility for future enhancements. In this specific case Ollama was used but it can be modified to work with GPT, Gemini and others AI. 
4. Overall Workflow

All of these contribute to reduce manual effort by automating data extraction and processing, Ensure high-quality outputs by leveraging advanced scraping and AI techniques and striking a balance between simplicity for the end-user and technical sophistication under the hood, ensuring both usability and effectiveness.




