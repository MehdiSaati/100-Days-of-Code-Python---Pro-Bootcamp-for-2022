from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By, Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

MY_FACEBOOK_USRNAME = ""
MY_FACEBOOK_PASSWORD = ""


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path ="C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
driver = webdriver.chrome(chrome_driver_path, chrome_options)
driver.get("http://www.tinder.com")
time.sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()
time.sleep(5)

facebook_login = driver.fine_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
facebook_login.click()
time.sleep(5)

# switch to the new pop-up window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

facebook_username = driver.find_element(By.XPATH, value='//*[@id="email"]')
facebook_username.send_keys(MY_FACEBOOK_USRNAME)

facebook_password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
facebook_password.send_keys(MY_FACEBOOK_PASSWORD)
facebook_password.send_keys(Keys.ENTER)

#  back on the Tinder page
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):
    time.sleep(2)
    try:
        print("call")
        like_button = driver.find_element(By.XPATCH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()







