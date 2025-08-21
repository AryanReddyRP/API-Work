import requests
from datetime import datetime

USERNAME = "aryanreddy0922"
TOKEN = "ij0iahv0h0902oin4409"   #custom token that we generated
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"

user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#used to create a user in pixela
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id" : graph_id,
    "name" : "Cycling Graph",
    "unit" : "km",
    "type": "float",
    "color" : "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today = datetime(year=2025, month=8, day=4)
pixel_parameters = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "13.5"
}

response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)