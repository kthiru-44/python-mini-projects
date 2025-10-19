##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# done

email = "pycharmtest.thiru@gmail.com"
password = "souo nief gwgs yrur"

# 2. Check if today matches a birthday in the birthdays.csv

import datetime as dt
import pandas
import random
import smtplib

tdy = dt.datetime.now()
day = tdy.day
mon = tdy.month

csv = pandas.read_csv("birthdays.csv")

birthday_dict = {(csv_row['month'],csv_row['day']): csv_row for (index,csv_row) in csv.iterrows()}


if (mon,day) in birthday_dict:
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt") as f :


        birthday_human = birthday_dict[mon,day]
        print(birthday_human)
        content = f.read()
        content.replace('[NAME]',birthday_human['name'])


        connect = smtplib.SMTP("smtp.gmail.com")
        connect.starttls()
        connect.login(user=email,password=password)
        connect.sendmail(from_addr=email,to_addrs=birthday_human['email'],msg=f"Subject:Happy Birthday !! \n\n {content}")
        connect.close()
