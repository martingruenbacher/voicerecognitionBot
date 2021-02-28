from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

import time
import os


def click(xpath):
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)


firefox_options = Options()
#firefox_options.add_argument("--headless")
firefox_options.add_argument("--enable-javascript")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.add_argument("--no-sandbox")
driver = webdriver.Firefox(options=firefox_options, executable_path="D:\\Dokumente\\web_scraping\\geckodriver.exe")

driver.get("https://open.spotify.com/")
wait = WebDriverWait(driver, 20)
# click anmelden
click("/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]")

# Login user and pass
wait.until(EC.element_to_be_clickable((By.ID, "login-username")))
element = driver.find_element_by_id("login-username")
element.send_keys("void122124@gmail.com")
element = driver.find_element_by_id("login-password")
element.send_keys("Martin2000")
element = driver.find_element_by_id("login-button")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

# cookie button
wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
element = driver.find_element_by_id("onetrust-accept-btn-handler")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

# click playbutton
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]")))
element = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

