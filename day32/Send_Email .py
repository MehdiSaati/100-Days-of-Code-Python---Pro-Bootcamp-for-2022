import smtplib

my_email  = "my_email@yahoo.com" 
my_password = "my_password"
receiver_email  = "mehdi.sz.developer@gmail.com"

try:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password=my_password)
        connection.sendmail(from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject:Hello\n\nThis is the body of my email."
        )
    print("Successfully sent email")

except :
    print("Error !")


 