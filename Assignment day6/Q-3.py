import requests

print("----- RANDOM USER -----")

user_url = "https://randomuser.me/api/"

user_data = requests.get(user_url).json()

user = user_data['results'][0]

print("Name :", user['name']['first'], user['name']['last'])
print("Email :", user['email'])
print("Country :", user['location']['country'])