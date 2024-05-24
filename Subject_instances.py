import time
import base64
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#file,link
def subject_instances():
    try:
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run Chrome in headless mode
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        link="https://handbook.latrobe.edu.au/subjects/2024/CSE1OOF"
        # Close the browser window
        driver.get(link)
        #time.sleep(10)  # Add a delay of 5 seconds

        #driver.execute_script("document.body.style.zoom = '80%'")

        # Find the dropdown menu by its position (assuming it's the third div element)
        #dropdown_menu = driver.find_element("xpath","//*[@id=\"academic-item-banner\"]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/button/div/div[2]")
        #dropdown_menu = driver.find_element("xpath","//*[@id=\"academic-item-banner\"]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div")
        dropdown_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"academic-item-banner\"]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/button/div/div[2]")))

        # Interact with the dropdown menu
        dropdown_menu.click()

        # Extract the text of the second dropdown option
        for i in range(2,400):
            xpath="//*[@id=\"offering_switcher_internal_nav\"]/ul/li["+str(i)+"]/a/div[2]"
            if len(driver.find_elements(By.XPATH, xpath)) > 0:
                menu = driver.find_element(By.XPATH, xpath)
                option_text = menu.text
                option_text = option_text.split('\n')
                # print(lines)
                option_text.extend(option_text)
                for i in option_text:
                    file.write(i)
                    file.write('\n')
                file.write('\n')
            else:
                break
    finally:
        print()
subject_instances()