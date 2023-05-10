from bs4 import BeautifulSoup
import requests
# import lxml
import re

product_url = "https://www.amazon.com/ALPINE-HEARING-PROTECTION-MotoSafe-Reusable/dp/B09RWXDG7V/ref=sr_1_2_sspa?keywords=alpine%2Bhearing%2Bprotection&qid=1683649407&sprefix=alpine%2Bhearing%2Caps%2C291&sr=8-2-spons&smid=A1N2X4ZOL32CTZ&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHQjA1RkswUU1LQ0EmZW5jcnlwdGVkSWQ9QTA5MzM1NzgyVlpCTDI5NUc3SDdaJmVuY3J5cHRlZEFkSWQ9QTAzMjQyNDIxQ0xBWFZSTkJLSlMyJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"

User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 " \
             "Safari/537.36"

Accept_Language = "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7"

headers = {'Accept-Language': Accept_Language,
           'User-Agent': User_Agent}

response = requests.get(product_url, headers=headers)


soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

get_price = soup.find(name="span", class_="a-offscreen").getText()

price_without_currency = get_price.split("$")[1]
m = re.findall(r'\d+\.\d+', price_without_currency)[0]

price_as_float = float(m)
print(price_as_float)
#########################################################################################
import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 22

if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_as_float}"

if price_as_float < 22:
    my_email = "tomtest75@yahoo.com"
    password = "qcckldniyayuprin"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="tomtest208@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}".encode("utf-8")
                            )
        connection.close()