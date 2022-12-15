import datetime as dt
import smtplib
import random
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day32/Send-Motivationa-Quotes")

MY_EMAIL = "my_email@yahoo.com" 
MY_PASSWORD= "my_password"
RECIVER_EMAIL  = "mehdi.sz.developer@gmail.com"

# Today Thursday
now = dt.datetime.now()
week_day = now.weekday()
if week_day == 3:
    with open("quotes.txt", "r") as quote_file:    
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    try:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL , password=MY_PASSWORD)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIVER_EMAIL,
            msg=f"Subject:Monday Motivation\n\n {quote}"
            )
        print("Successfully sent email")

    except :
        print("Error!")
else:
    print("Faild")
