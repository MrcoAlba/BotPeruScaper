import requests
import json

def RequestData(url, file):
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        # Save the JSON data to a file
        with open(file, 'w') as file:
            json.dump(json_data, file)
        return True
    
    else:
        return False
