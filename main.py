import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()

sender = "gocmenkaanmert12@gmail.com"
receiver = "gocmenmertkaan@gmail.com"
password = "tvsiblmtjwsedgnj"


def sending():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(sender, receiver, msg="Subject:ISS CLOSING YOU! Hey yo\n\n Look sky")

while True:
    time.sleep(60)
    if int(iss_latitude) - int(MY_LAT) > 5 or int(MY_LAT) - int(iss_latitude) > 5 :
        if int(iss_longitude) - int(MY_LONG) > 5 or int(MY_LONG) - int(iss_longitude) > 5:
            if int(time_now.hour) < sunrise:
                if int(time_now.hour) > sunset:
                    sending()






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



