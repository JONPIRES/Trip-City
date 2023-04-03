import requests 
from flask import Flask, render_template
import os
api_key = os.getenv('API_KEY')

api_key = os.getenv('API_KEY')


# auto-complete (GET method)

url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"

querystring = {"query":"New York","lang":"en_US","units":"km"}

headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

object = response.json()

text = f" this is the object name: {object['data']['Typeahead_autocomplete']['results'][4]}"

print(response.text)

# Locations search POST


# url = "https://travel-advisor.p.rapidapi.com/locations/v2/search"

# querystring = {"currency":"USD","units":"km","lang":"en_US"}

# payload = {
# 	"query": "chiang mai",
# 	"updateToken": ""
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
# }

# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

# print(response.text)


# Search Nearby


# url = "https://travel-advisor.p.rapidapi.com/locations/v2/list-nearby"

# querystring = {"currency":"USD","units":"km","lang":"en_US"}

# payload = {
# 	"contentId": "cc8fc7b8-88ed-47d3-a70e-0de9991f6604",
# 	"contentType": "restaurant",
# 	"filters": [
# 		{
# 			"id": "placetype",
# 			"value": ["hotel", "attraction", "restaurant"]
# 		},
# 		{
# 			"id": "minRating",
# 			"value": ["30"]
# 		}
# 	],
# 	"boundingBox": {
# 		"northEastCorner": {
# 			"latitude": 12.248278039408776,
# 			"longitude": 109.1981618106365
# 		},
# 		"southWestCorner": {
# 			"latitude": 12.243407232845051,
# 			"longitude": 109.1921640560031
# 		}
# 	}
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": api_key,
# 	"X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
# }

# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

# print(response.text)