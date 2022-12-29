import requests
from bs4 import BeautifulSoup

import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day45/scrape_finance")

URL = "https://www.tgju.org"

response = requests.get(URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

finance = [item.getText() for item in soup.find_all(name="span", class_="info-price")]
borse = finance[0]
gold_18 = finance[3]
coin = finance[4]
dollar = finance[5]

with open("finance.txt", mode="w") as file:
    file.write(f"borse : {borse}\ngold-18 : {gold_18}\ncoin : {coin}\ndollar : {dollar}")

 
 