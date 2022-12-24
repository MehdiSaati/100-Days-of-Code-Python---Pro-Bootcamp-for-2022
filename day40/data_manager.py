import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/*************************/flightDeals/prices/"
 
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/*********************************/flightDeals/users"
 

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

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

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
    

    def save_user(self, first_name, last_name, email):
        """Takes the user's details as STRs and add them to the worksheet."""
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        self.headers = {
            "Authorization": "Bearer 5kljkk55jhgfvbn88"
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body, headers=self.headers)
        response.raise_for_status()
        # also to have some feedback
        print(f"User {first_name} {last_name} has been added to worksheet.")