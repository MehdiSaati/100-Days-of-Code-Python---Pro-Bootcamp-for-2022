from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

URL =  "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

http_headers = {
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}

response = requests.get(URL, http_headers)
 
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options)

web_html = response.text
soup = BeautifulSoup(web_html, "html.parser")
search_results = soup.find("div", {"id": "grid-search-results"})

 
def get_links():
    links_list = [a["href"] for a in search_results.find_all("a", tabindex="0")]
    for index in range(len(links_list)):
        if not links_list[index].startswith("http"):
            links_list[index] = 'https://www.zillow.com' + links_list[index]
    return links_list


def get_addresses():
    address_list = [address.getText() for address in search_results.find_all("a", tabindex="0") if address.getText()]
    return address_list


def get_price():
    price_list = [price.getText()[:7] for price in soup.find_all("div", class_="list-card-price")]
    return price_list


GOOGLE_FORMS = "GOOGLE_FORMS"
driver.get(GOOGLE_FORMS)
time.sleep(3)

print(len(get_addresses()))
for fill_out in range(len(get_addresses())):
    property_address = driver.find_element(
        By.XPATH, value='//*[@aria-describedby = "i2 i3"]')
    property_price = driver.find_element(
        By.XPATH, value='//*[@aria-describedby = "i6 i7"]')
    property_link = driver.find_element(
        By.XPATH, value='//*[@aria-describedby = "i10 i11"]')

    property_address.send_keys(get_addresses()[fill_out])
    property_price.send_keys(get_price()[fill_out])
    property_link.send_keys(get_links()[fill_out])
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()
 

