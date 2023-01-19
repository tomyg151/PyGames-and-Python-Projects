
import pandas
import datetime as dt
import random
import smtplib


# 1. Update the birthdays.csv

data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient='records')  # convert to list of many dicta's, each dicta's
# contain the data in the row in the pandas
list_of_Birthdays = []
for date in range(len(data_list)):
    month = data_list[date]['month']
    day = data_list[date]['day']
    birthday = (month, day)
    list_of_Birthdays.append(birthday)



# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
current_date = (month, day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
LETTER_1 = "letter_templates/letter_1.txt"
LETTER_2 = "letter_templates/letter_2.txt"
LETTER_3 = "letter_templates/letter_3.txt"
list_of_letter = [LETTER_1, LETTER_2, LETTER_3]
random_letter = random.choice(list_of_letter)  # choose random letter from the list letters (list_of_letter)


if current_date in list_of_Birthdays:
    for date in range(len(data_list)):
        if (data_list[date]['month'], data_list[date]['day']) == current_date:
            current_name = data_list[date]['name']  # find current name with the birthday
            current_address = data_list[date]['email']  # find the current mail of the

    with open(random_letter) as letter_file:
        letter_content = letter_file.read()
        new_letter = letter_content.replace('[NAME]', current_name)

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "tomtest208@gmail.com"
        password = "elkepfdvqdpbhwvj"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=current_address,
                                msg=f"subject:Happy Birthday!\n\n{new_letter}")



