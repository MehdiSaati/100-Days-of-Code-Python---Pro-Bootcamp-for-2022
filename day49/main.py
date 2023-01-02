from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

MY_EMAIL = ""
MY_PASSWORD = ""
MY_NUMBER = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path ="C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3310309880&f_AL=true&f_WT=2&geoId=92000000&keywords=python%20developer&location=Worldwide&refresh=true")

# Sign-in

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()
time.sleep(2)
email = driver.find_element(By.ID, 'username')
email.send_keys(MY_EMAIL)
password = driver.find_element(By.ID, 'password')
password.send_keys(MY_PASSWORD)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "div button").click()
time.sleep(5)


# Scan available jobs
# job_listings  = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
job_listings  = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

jobs_available = [job.text for job in job_listings ]
 
print(jobs_available)

#Select job posting and click on apply
while jobs_available:
    posting_num = 0
    try:
        driver.find_element(By.LINK_TEXT, f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button--top-card").click()
    except NoSuchElementException:
        posting_num += 1
        driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
        time.sleep(2)
        driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button").click()
    finally:
        # Complete application
        jobs_available.remove(jobs_available[posting_num])
        try:
            time.sleep(2)
            phone_num = driver.find_element(by=By.CLASS_NAME, value='artdeco-text-input--input')
            phone_num.clear()
            time.sleep(2)
            phone_num.send_keys(MY_NUMBER)
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='.artdeco-button').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='.artdeco-modal__confirm-dialog-btn').click()
            time.sleep(2)
            driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Submit application"]').click()
        except NoSuchElementException:
            print('Cannot apply, skipped')
    print("Work complete")