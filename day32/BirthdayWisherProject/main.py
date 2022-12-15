import pandas
from datetime import datetime
import smtplib
import random
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day32/BirthdayWisherProject")

PLACEHOLDER = "[RECEIVER_NAME]"
SENDER_NAME = "[SENDER_NAME]"
MY_EMAIL = "my_email@yahoo.com" 
MY_PASSWORD = "my_password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[(today_tuple)]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person["name"])
        contents = contents.replace(SENDER_NAME, "mehdi")
    try :
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL , password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL ,
                to_addrs=birthday_person["email"] ,
                msg=f"Subject:Happy Birthday\n\n{contents}"
                )
            print("Successfully sent email")
    except:
        print("Error!")
