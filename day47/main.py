#  Create an Automated Amazon Price Tracker
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = " "
MY_PASSWORD = " "
TO_EMAIL = " "
URL = "https://www.amazon.com/PlayStation-5-Console/dp/B0BCNKKZ91/ref=d_pd_sbs_sccl_3_3/138-2028085-5986928?pd_rd_w=OeROO&content-id=amzn1.sym.38bbd1de-73a5-4ef9-9954-df27c3112829&pf_rd_p=38bbd1de-73a5-4ef9-9954-df27c3112829&pf_rd_r=D32ZE1ZA87WSD5Q73HGQ&pd_rd_wg=5rbpp&pd_rd_r=ee7c8ba9-2354-4f6d-91c9-9f259cac49e0&pd_rd_i=B0BCNKKZ91&psc=1"

http_headers = {
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}
response = requests.get(URL, headers=http_headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
product_name = " ".join(
    soup.find(name="span", class_="a-size-large product-title-word-break", id="productTitle").getText().split())

if price < 500.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Alert: Amazon Price Tracker\n\n{product_name}\nis now ${price}.\n\n{URL}",
        )
