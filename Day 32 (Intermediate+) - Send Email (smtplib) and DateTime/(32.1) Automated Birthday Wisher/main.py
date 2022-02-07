##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
from datetime import datetime
from random import randint
import smtplib

MY_EMAIL = "sajepan.dev@gmail.com"
MY_PASSWORD = "-Password-"

# TODO: 1. Create a tuple from today's date with datetime
today = datetime.now()
today_tuple = (today.month, today.day)

# TODO: 2 read csv file with pandas
data = pd.read_csv("birthdays.csv")

# TODO: 3 Create a dictionary with comprehension
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# TODO: 4. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    # TODO: 5. If step 4 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    # TODO: 3. Send the letter generated in step 3 to that person's email address.
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    print(birthday_person["name"])
    # TODO: 4. Send email with the
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg=f'Subject: Happy Birthday {birthday_person["name"]}!\n\n{contents}'
        )







