import requests
from datetime import datetime
import smtplib

# Sending email details
my_email = 'medemo760@gmail.com'
password = 'AAAaaa111pass'
to_addrs = 'medemo760@gmail.com'

MY_LAT = -33.800770 # Your latitude
MY_LONG = 151.179596 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
MY_LAT = iss_latitude
MY_LONG = iss_longitude
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

print(iss_longitude, iss_longitude)
print(sunrise,sunset)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
print(time_now.hour)
if iss_longitude - 5 < MY_LONG and iss_longitude + 5 > MY_LONG and iss_latitude - 5 < MY_LAT and iss_latitude + 5 > MY_LAT:
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print("sending email...")
        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_addrs,
                msg= f'Subject:Look Up from your screen!\n\nLook up from your screen and see the world! The ISS is above you!\n The sunrise today is at: {sunrise} oclock \nSunset is:{sunset} oclock'
            )


