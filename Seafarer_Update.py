import requests
import json
from requests.auth import HTTPBasicAuth

# Define the URL
url = 'https://xpressfeeders.cloudfleetmanager.com/papi/Crewing/Seafarers' #url

# Create the data (same JSON body as you provided)
data = [
    {
        "FirstName": "Celia", 
        "Surname": "Kang", 
        "ID": 3876,
        "Rank": "Chief Engineer",
        "Nationality": "Singaporean", 
        "Sex": "F",
        "SyncID": 1,
        "ShoeSize": "42",
        "AgencyData": {
            "City": "Mumbai",
            "Name": "Eastaway (India) Private Limited"
        }   
    }
]

# Set your username and password
username = 'Subramaniyam'
password = 'Subu2023$'

# Headers, if any, can be added here. For example, to send JSON
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request with Basic Authentication
response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    print("Success:", response.json())  # Print the response from the API
else:
    print("Failed to post:", response.status_code, response.text)
