import requests
import json

url = ("https://apiv3.apifootball.com/?action=get_countries&APIkey=a1f6f775905ed5919f070c3d1057209045b2c65ba35cff7abb47804b640b1458")
response = requests.get(url)
print(response.json())