import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 32.398359  # Your latitude
MY_LONG = 34.933848  # Your longitude

MY_EMAIL = "tomtest208@gmail.com"
PASSWORD = "elkepfdvqdpbhwvj"

def is_night():
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

    time_now = datetime.now().hour
    # and it is currently dark
    if sunrise < time_now < sunset:
        return True
    return False

# print(time_now.hour)
# print(sunrise)
# print(sunset)

def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.


    # iss is close to our current location?
    # If the ISS is close to my current position
    if (iss_longitude + 5 >= MY_LONG or iss_longitude - 5 <= MY_LONG and
            iss_latitude + 5 > MY_LAT or iss_latitude - 5 < MY_LAT):
        return True
    return False

while True:
    # run the code every 60 seconds
    time.sleep(60)
    if iss_is_close() and is_night():
        # Then send me an email to tell me to look up.

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"subject:look up👆☝!\n\nMay you will see Know the ISS station in the sky!")




