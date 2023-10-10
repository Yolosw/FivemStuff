import requests

ip = input("Ip Address of the server: ")
url = "http://"+ ip + ":30120/players.json"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    for x in json_data:
        id_value = x.get("id")
        namn_value = x.get("name")
     
        if id_value is not None and namn_value is not None:
            print(f"Ids: {id_value} Name: {namn_value}")
        else:
            print("No ids found")
else:
    print(f"Error: Status code {response.status_code}")