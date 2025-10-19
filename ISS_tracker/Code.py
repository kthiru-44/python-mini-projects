
import requests
from datetime import datetime
import smtplib
import time

email = ""
password = ""


MY_LAT = 
MY_LNG = 

def its_there():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    isla1 = (MY_LAT - 5)
    isla2 = (MY_LAT + 5)
    isln1 = (MY_LNG - 5)
    isln2 = (MY_LNG + 5)


    if isla2 >= iss_latitude >= isla1 and isln2 >= iss_longitude >= isln1 :
        return True
    return None

def is_night():

    parameter = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "tzid":"Indian/Mahe"
    }

    now = datetime.now().hour

    res = requests.get(url="https://api.sunrise-sunset.org/json?formatted=0",params=parameter)
    res.raise_for_status()

    data = res.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if now > sunset and now < sunrise :
        return True
    return None

while True :
    time.sleep(60)

    if its_there() and is_night() :

        connect = smtplib.SMTP("smtp.gmail.com")
        connect.starttls()
        connect.login(user=email, password=password)
        connect.sendmail(from_addr=email, to_addrs="ur_email", msg=f"Subject:Look Up  \n\n The ISS is here . Look up ")
        connect.close()




