import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CODEFORCES_URL = "https://codeforces.com/"

def create_mashup(problems, MASHUP_NAME, MASHUP_DURATION, USERNAME, PASSWORD):
    # Navigate to codeforces and login
    driver = webdriver.Firefox()
    driver.get(CODEFORCES_URL + "enter")
    assert "Codeforces" in driver.title
    usernameField = driver.find_element(By.ID, "handleOrEmail")
    usernameField.send_keys(USERNAME)
    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys(PASSWORD)
    passwordField.submit()

    # Navigate to new mashup page
    WebDriverWait(driver, 5).until(EC.url_to_be(CODEFORCES_URL))
    driver.get(CODEFORCES_URL + "mashup/new")
    mashupNameField = driver.find_element(By.ID, "contestName")
    mashupNameField.send_keys(MASHUP_NAME)
    mashupDuration = driver.find_element(By.ID, "contestDuration")
    mashupDuration.send_keys(str(MASHUP_DURATION))

    for problemName in problems:
        problemField = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "problemQuery")))      
        problemField.send_keys(problemName)
        problemField.send_keys(Keys.RETURN)

    time.sleep(1) # We need to have a short pause before submitting
    submitButton = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit")))
    submitButton.submit()

    # input("Press Enter to close...")
    driver.close()
