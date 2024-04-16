import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def pdf_download(link,filename):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    time.sleep(2)
    pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
    pdf_data = base64.b64decode(pdf["data"])
    with open(filename, "wb") as f:
        f.write(pdf_data)