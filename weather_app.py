import json
import os
import win32com.client as win32
import requests
city =input("ENTER YOUR CITY HERE")
url= f"https://api.weatherapi.com/v1/current.json?key=9a8f4cacbc16460cb2393829231708&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
x= wdic["current"]["temp_c"]
print(x,"C")
speak = win32.Dispatch("SAPI.Spvoice")
speak.Speak(f"THE CURRENT weather in {city} is {x} degree celcius")


