import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/de392ba0f59fefb2ae9c68e9a2300bb9/copyOfFlightDeals/users"

print("Welcom to Tom's flight club. \nWe found the best deals and email you.")
first_name = input("What is your first name:")
last_name = input("What is your last name:")
email = input("What is your Email:")
check_email = input("email verification:")

if email == check_email:
    print("You're in the club!")

    headers = {
        "Username": "tomy",
        "Password": "tomy_kod"
    }

    users = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(
        url=f"{SHEETY_PRICES_ENDPOINT}",
        json=users,
        headers=headers
    )
    print(response.text)
    print("success! your email as added to the club data.")
