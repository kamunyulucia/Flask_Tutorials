#!/bin/python

#getting weather of major cities around the world using OpenWeather API

import requests
import json

#API key from open weather map
api_key = "07cffe6d6e74f990e56c427e275b3fe1"

#base url from open weather map
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("please enter your favorite city name : ") 

complete_url = base_url + "appid=" + api_key + "&q" + city_name

#use request to get the data

response =  requests.get(complete_url)
#print(response)
data = response.json() # converting the response into json data format

print(data)
