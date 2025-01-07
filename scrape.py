from selenium.webdriver.chrome.service import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
import streamlit as st
import os

SBR_WEBDRIVER = 'brd-customer-hl_ff81bf84-zone-ai_mapaula_scraper:mzmixte3n2h7'
   
def scrape_website(website):
    print("Connecting to the website...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection,options=ChromeOptions()) as driver:
        print('Connected! Navigating to the website...')
        driver.get('website')
        #Captcha
        print('Waiting for the Captcha to be solved...')
        solve_res = driver.execute('executeCdpCommand', 
        {
            'cmd': 'Captcha.waitForSolve', 
            'params': {'detectTimeout':10000},
        })
        print ('Captcha solved:', solve_res['result']['status'])
        print ('Navigated! Scraping the website...')
        html = driver.page_source
        print (html)
        return(html)

def extract_body_content(html_content):
    print("Extracting the body content...")
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return "No body content found!"

def clean_body_conent(body_content):
    print("Cleaning the body content...")
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_lenght =6000):
    return [
        dom_content[i:i + max_lenght] for i in range(0, len(dom_content), max_lenght)
    ]
    
if "dom_content" in st.session_state.dom_content:
    parse_description = st.txt_area("Descrbe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the DOM content")

            dom_chunks = split_dom_content(st.session_state.dom_content)

