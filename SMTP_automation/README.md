Automated Birthday Wisher (SMTP + CSV)

This Python script automates the process of sending birthday wishes via email using the SMTP protocol. It reads a list of people and their birthdays from a CSV file, and if someone's birthday matches the current date, it sends them a randomly chosen birthday greeting email.

## Features

- Reads birthday data from a CSV file
- Automatically checks if today matches any birthday
- Randomly selects a birthday letter template
- Sends the greeting via email using SMTP
- Easy to customize for your own contacts and email account

## How It Works

1. The `birthdays.csv` file contains name, email, and birth date information.
2. On running the script, it checks whether today's month and day match any entry.
3. If there’s a match:
   - A random template is chosen from the `letter_templates/` folder
   - The name placeholder `[NAME]` is replaced with the recipient’s name
   - An email is sent using your SMTP credentials


## Requirements

- Python 3.x
- An email account that allows SMTP access (e.g., Gmail, Outlook)
- Internet connection

## How to Run

1. Update the `birthdays.csv` file with your data.
2. Set your email and password in the script (use environment variables or a `.env` file for security).
3. Run the script:

```bash
python main.py
