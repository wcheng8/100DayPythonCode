import smtplib
import datetime as dt
import pandas as pd
import random

# Sending email details
my_email = 'medemo760@gmail.com'
password = 'AAAaaa111pass'

# 1. Update the birthdays.csv
birthdays = pd.read_csv('./birthdays.csv')
birthday_data = birthdays.to_dict('records')
with open('./quotes.txt') as quote_file:
    quotes = quote_file.readlines()


# 2. Check if today matches a birthday in the birthdays.csv
time = dt.datetime.now()
time_month = time.month
time_day = time.day

for birthday in birthday_data:
    if birthday['month'] == time_month and birthday['day'] == time_day:
        to_addrs = birthday['email']
        randomnumber = random.randint(1,3)
        # random motivational quote
        motivation = random.choice(quotes)
        # Construct random birthday template
        with open(f'./letter_templates/letter_{randomnumber}.txt') as letter_temp:
            letter = letter_temp.readlines()
        heading = letter[0].replace('[NAME]', birthday['name'])
        message = [heading]
        message += letter[1:]
        message_str = ''.join(message)
        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_addrs,
                msg=f'Subject:Happy Birthday {birthday["name"]}\n\n {message_str}\n\n{motivation}'
            )



