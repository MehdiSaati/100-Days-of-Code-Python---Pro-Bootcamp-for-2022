#Usin chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
# chrome_driver_path="C:\Development\chromedriver.exe"

# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count)


# ---------------------------Using FirFox ----------------------------

driver = webdriver.Firefox()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# # article_count.click()

# all_portals = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
# # all_portals.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name= driver.find_element_by_name("fName")
first_name.send_keys("my first name")
last_name= driver.find_element_by_name("lName")
last_name.send_keys("my last name")
email= driver.find_element_by_name("email")
email.send_keys("my email")

submit = driver.find_element_by_css_selector("form button")
submit.click()




