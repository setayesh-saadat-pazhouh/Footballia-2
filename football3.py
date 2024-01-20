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
    print("")
    choice = input("Do you have another choice? ")
    print("")
    if choice == "2":
        print("Competitions:")
        print("")

        url = "https://apiv3.apifootball.com/?action=get_leagues&country_id=6&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
        response = requests.get(url)
        data = response.json()
        for league in data:
            print(league['league_name'])
        print("")
        choice = input("Do you have another choice? ")
        print("")

    elif choice == "3":
        print("Teams:")
        print("")

        url = "https://apiv3.apifootball.com/?action=get_teams&league_id=302&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
        response = requests.get(url)
        data = response.json()
        for team in data:
            print(team['team_name'])
        print("")
        choice = input("Do you have another choice? ")
        print("")

    elif choice == "4":
        print("Players:")
        print("")

        url = "https://apiv3.apifootball.com/?action=get_players&player_name=Ronaldo&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
        response = requests.get(url)
        data = response.json()
        for player in data:
            print(player['player_name'])
        print("")
        choice = input("Do you have another choice? ")
        print("")

    elif choice == "5":
        print("Standings:")
        print("")

        url = "https://apiv3.apifootball.com/?action=get_standings&league_id=152&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
        response = requests.get(url)
        data = response.json()
        for standings in data:
            print(standings['standings_name'])
        print("")
        choice = input("Do you have another choice? ")
        print("")

    elif choice == "6":
        print("Exit:")
        print("")
        print("Hope to enjoy:)")
        quit()


elif choice == "2":
    print("Competitions:")
    print("")

    url = "https://apiv3.apifootball.com/?action=get_leagues&country_id=6&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
    response = requests.get(url)
    data = response.json()
    for league in data:
        print(league['league_name'])
    print("")
    choice = input("Do you have another choice? ")
    print("")

elif choice == "3":
    print("Teams:")
    print("")

    url = "https://apiv3.apifootball.com/?action=get_teams&league_id=302&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
    response = requests.get(url)
    data = response.json()
    for team in data:
        print(team['team_name'])
    print("")
    choice = input("Do you have another choice? ")
    print("")

elif choice == "4":
    print("Players:")
    print("")

    url = "https://apiv3.apifootball.com/?action=get_players&player_name=Ronaldo&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
    response = requests.get(url)
    data = response.json()
    for player in data:
        print(player['player_name'])
    print("")
    choice = input("Do you have another choice? ")
    print("")

elif choice == "5":
    print("Standings:")
    print("")

    url = "https://apiv3.apifootball.com/?action=get_standings&league_id=152&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458"
    response = requests.get(url)
    data = response.json()
    for standings in data:
        print(standings['standings_name'])
    print("")
    choice = input("Do you have another choice? ")
    print("")

elif choice == "6":
    print("Exit:")
    print("")
    print("Hope to enjoy:)")
    quit()