# Habit Tracker using pixela
from datetime import datetime
import requests
pixela_endpoint = 'https://pixe.la/v1/users'
pixela_token = 'aft123Zabc'
user = 'wcheng1337'
# Create user
user_params = {
    'token': pixela_token,
    'username': user,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# request = requests.post(url=pixela_endpoint, json = user_params)
# print(request.json())

# https://pixe.la/@wcheng1337
# Create graph
token_header = {
    'X-USER-TOKEN': pixela_token
}
graph_id = 'poopgraph1'
# graph_param = {
#     'id': graph_id,
#     'name': 'poopgraph',
#     'unit': 'grams',
#     'type': 'float',
#     'color': 'shibafu'
# }
# graph_req = requests.post(url=f'{pixela_endpoint}/{user}/graphs', json= graph_param,headers=token_header)
# print(graph_req.json())

# Graph @ https://pixe.la/v1/users/wcheng1337/graphs/poopgraph1
# Post to graph
today = datetime.now()
user_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '2.5'
}
# postvalue_request = requests.post(url=f'{pixela_endpoint}/{user}/graphs/{graph_id}', headers=token_header,json=user_data)
# print(postvalue_request.json())

# update a graph point
update_data = {
    'quantity': '250'
}
update_req = requests.put(url=f'{pixela_endpoint}/{user}/graphs/{graph_id}/{today.strftime("%Y%m%d")}', headers=token_header,json=update_data)
print(update_req.json())