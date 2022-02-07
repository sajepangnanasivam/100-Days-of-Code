import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "sajepan.dev@gmail.com"
MY_PASSWORD = "_Password_"
MY_LAT = 60.035915
MY_LNG = 11.125331


# --------------- FUNCTIONS --------------#
def iss_is_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# --------------- ISS API --------------#
# Getting the ISS data
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# For testing
# iss_latitude = float(MY_LAT + 5)
# iss_longitude = float(MY_LNG - 4)

while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up\n\nThe ISS is above you in the sky!"
        )
        print("Email Sent!")
