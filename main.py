# https://docs.pixe.la
# https://pixe.la
import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "dfuhjhdfjh123"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": "JKR005tnfP",
    "username": "username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "KM",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Posting a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

activity_date = datetime.now()
formatted_date = activity_date.strftime("%Y%m%d")

pixel_config = {
    "date": formatted_date,
    "quantity": input("How many kilometers did you run today? ")
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

 # Updating a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"

update_config = {
    "quantity": "1.5",
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

# Deleting a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
response = requests.delete(url=update_pixel_endpoint, json=update_config, headers=headers)
print(response.text)