ISS Overhead Notifier (Python + SMTP + APIs)

This Python script sends you an email notification when the International Space Station (ISS) is passing overhead at your location **and** it’s currently dark outside, so you can look up and try to spot it.

## How It Works

1. **ISS Location Check**  
   Uses the Open Notify ISS API (`http://api.open-notify.org/iss-now.json`) to fetch the current position of the ISS. If the ISS is within ±5° latitude and longitude of your location, it qualifies as "overhead".

2. **Nighttime Check**  
   Uses the Sunrise-Sunset API (`https://api.sunrise-sunset.org/json`) to check whether it's currently dark at your location by comparing your local hour with the API-provided sunrise and sunset times.

3. **Email Notification**  
   If both conditions are true, the script sends an email using Gmail’s SMTP server with a simple message:  
   `"The ISS is here. Look up!"`


## Requirements

- Python 3.x
- Internet connection
- Gmail account with SMTP access enabled
- Required libraries:
  - `requests`
  - `datetime`
  - `smtplib`

Install dependencies using:
```bash
pip install requests
