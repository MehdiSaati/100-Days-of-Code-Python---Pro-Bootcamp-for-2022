# Habit Tracker
import requests
from datetime import datetime

USERNAME = "mehdi-know"
TOKEN = "medijhjgfgfvbfdddffdfhhjjkkklpiytredghjkl"
GRAPGH_ID = "graph1"

user_param = {
    "token":TOKEN,
    "username":USERNAME, 
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    }
pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPGH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
    }
headers ={
    "X-USER-TOKEN" : TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}"

today = datetime.now()
# today = datetime(year=2022,month=12,day=19)
# print(today.strftime("%Y%m%d"))
 
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycle today?")
    }
pixel_creation_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_creation_response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}/20221220"
new_pixel_data = {
    "quantity":"5.75"
    }
# pixel_update_response = requests.put(pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(pixel_update_response.text)


pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}/20221220"

# pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)
