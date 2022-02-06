import smtplib
import datetime as dt
import random

my_email = "sajepan.dev@gmail.com"
password = "SajeeSobi271018"

now = dt.datetime.now()
weekday = now.weekday()

with open(file="quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)

# Connection to the smtp server
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Transport layer security - Securing the connection
    connection.starttls()
    connection.login(user=my_email, password=password)
    # If Weekday is equal to Saturday
    if weekday == 5:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sajepan.dev@yahoo.com",
            msg="Subject: Saturday Motivation"
                f"\n\n{random_quote}"
            )
    connection.close()