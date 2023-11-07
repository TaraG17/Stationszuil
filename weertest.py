import requests

api_key = "befce6c12cc4de8793e5f9de6f2ace3a"
locatie = "Utrecht"
resource_uri = f"https://api.openweathermap.org/data/2.5/weather?q={locatie}&appid={api_key}"
response = requests.get(resource_uri)
response_data = response.json()

weather = response_data['weather'][0]['description']
temp = response_data['main']['temp']-272.15
print("The weather today has", weather, "with a temperature of", round(temp), "degrees.")
#later per ding uitlezen main -> temp

# for key in response_data.keys():
#     print(f"{key}: {response_data[key]}")
#print(round(temp, 1))
