import requests
import smtplib 

STOCK_NAME = "TSCO"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = "your api key"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your api key"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
# response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo")
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [ value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price)- float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down ="+"
else:
    up_down = "-"

diff_percent = round(difference / float(yesterday_closing_price)) * 100

if abs(diff_percent) < 4 :
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "from": "2022-11-20",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline:{article['title']}.\nBerif:{article['description']}" for article in three_articles]
    print(formatted_articles)
    for article in formatted_articles:
        try:
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user="Your Email" , password="Your Password")
                connection.sendmail(
                    from_addr="Your Email",
                    to_addrs="Your Email",
                    msg=f"Subject: Tesla Trade\n\n {article}"
                )
                print("Successfully sent email")
        except :
            print("Error!")
 