import json

import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Full data from Orbit:", data)

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    print(
        f"\n The Space Station is currently at latitude {latitude}, longitude{longitude}"
    )
    with open("day_20/iss_telemetry.json", "w") as f:
        json.dump(data, f, indent=4)
    print(" Live satellite telemetry saved to day_20/iss_telemetry.json!")
else:
    print(f"Failed to reach satellite: Status {response.status_code}")
