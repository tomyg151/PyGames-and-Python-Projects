from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/de392ba0f59fefb2ae9c68e9a2300bb9/copyOfFlightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/de392ba0f59fefb2ae9c68e9a2300bb9/copyOfFlightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.get_user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.get_user_data = data['users']
        return self.get_user_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
