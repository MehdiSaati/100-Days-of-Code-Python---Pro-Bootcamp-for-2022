import requests
from twilio.rest import Client

#TODO 1. Get yesterday's closing stock price

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = "your api key"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your api key"

TWILIO_SID = "your twilio sid"
TWILIO_AUTH_TOKEN ="your auth token"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [ value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. GET the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

#TODO 3. -Finishth positive difference between 1 and 2
difference = float(yesterday_closing_price)- float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down ="⬆️"
else:
    up_down = "⬇️"

#TODO 4. -Work out the value of 5% of yesterday's closing price
diff_percent = round(difference / float(yesterday_closing_price)) * 100

#TODO 5. -If TODO4 percentage is grater than 5 then print("Get News")
if abs(diff_percent) < 4 :
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    #TODO 6. -Create news API   
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    #TODO 7. -Use python slice operator a list that contain the first 3 articles hint
    three_articles = articles[:3]

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comperhension
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline:{article['title']}.\nBerif:{article['description']}" for article in three_articles]

    #TODO 9. -Send each article as a seprate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="your number",
            to="to number"
        )

