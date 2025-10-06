import requests
import datetime as dt
import smtplib
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
def night_time():
    current_time = dt.datetime.now().time().strftime("%H:%M:%S")
    parameter = {"lat": MY_LAT , "lng": MY_LONG, "formatted": 0}
    response=requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    sunrise=response.json()['results']['sunrise'].split('T')[1].split("+")[0]
    sunset=response.json()['results']['sunset'].split('T')[1].split("+")[0]

    if sunset< current_time < sunrise:
        return True
    else:
        return False


def day_time():
    current_time = dt.datetime.now().time().strftime("%H:%M:%S")
    parameter = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    sunrise = response.json()['results']['sunrise'].split('T')[1].split("+")[0]
    sunset = response.json()['results']['sunset'].split('T')[1].split("+")[0]

    if sunrise <current_time < sunset:
        return True
    else:
        return False

# EMAIL SENDER
def email_day():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs= EMAIL,
                            msg="Subject: ISS Notification\n\n The ISS is now in your location! Go out and take a look"
                            )
def email_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs= EMAIL,
                            msg="Subject: ISS Notification\n\n The ISS passed by while you were sleeping! Catch it next time!"
                            )

def task():
     if night_time():
        if (abs(float(latitude) - MY_LAT ) < 5) and (abs(float(longitude) - MY_LONG) < 5):
            email_night()
     elif day_time():
        if (abs(float(latitude) - MY_LAT ) < 5) and (abs(float(longitude) - MY_LONG) < 5):
            email_day()

task()





