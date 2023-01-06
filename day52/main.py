from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "airgun"
USERNAME = ""
PASSWORD = ""

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.XPATH, '')
        password = self.driver.find_element(By.XPATH, '')

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_follow_button = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for button in all_follow_button:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()








class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path, chrome_options=chrome_options)

        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        time.sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH,
                                   value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                 value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f"Download = {self.down} Mbps")
        print(f"Upload = {self.up} Mbps")

        time.sleep(2)
        bot.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)  
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?")
        time.sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
        time.sleep(2)
        self.driver.quit()
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed(SPEED_TEST_PATH)


