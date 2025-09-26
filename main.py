import requests
import datetime as dt
import smtplib
import time
import os

EMAIL = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASS"]

MY_LAT= 38.907192
MY_LONG= -77.036873
MY_EMAIL = "oyeludeferanmi@gmail.com"

# ISS_REQUESTS
iss_location= requests.get(url="http://api.open-notify.org/iss-now.json")
iss_location.raise_for_status()
data = iss_location.json()["iss_position"]
latitude = data["latitude"]
longitude = data["longitude"]
print(latitude)
# SUNRISE AND SUNSET REQUESTS
parameter = {"lat": MY_LAT , "lng": MY_LONG, "formatted": 0}
time=dt.datetime.now().time().strftime("%H:%M:%S")
response=requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
sunrise=response.json()['results']['sunrise'].split('T')[1].split("+")[0]
sunset=response.json()['results']['sunset'].split('T')[1].split("+")[0]


# EMAIL SENDER
def email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password= PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= MY_EMAIL,
                            msg="Subject: ISS Notification\n\n The ISS is now in your location! Go out and take a look"
                            )
def task():
    if (0<(float(latitude) - MY_LAT )< 5  or (0<MY_LAT - float(latitude) < 5)) and ((0<float(longitude) - MY_LONG < 5) or (0<MY_LONG- float(longitude) < 5)):
        if sunrise < time < sunset:
            email()
    else:
        print("Not yet!")

task()
