import requests
import json

print("")
print("Hello and Welcome to Footballia!")
print("First choose your request and then enter your choice")
print("")
print("1. Countries")
print("2. Competitions")
print("3. Teams")
print("4. Players")
print("5. Standings")
print("6. Exit")
print("")
choice = input("Please enter your choice: ")
print("")


if choice == "1":
    print("Countries:")
    print("")

    url = "https://apiv3.apifootball.com/?action=get_countries&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
    response = requests.get(url)
    data = response.json()
    for country in data:
        print(country['country_name'])


