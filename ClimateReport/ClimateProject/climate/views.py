from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(req):
    if req.method == "POST":
        city=req.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8892dd87c2f165dca3be010ece07b05b') .read()
        list_data=json.loads(source)
        data={
            "country_code" : str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon'])+ ',' + str(list_data['coord']['lat']),
            "temp": str(list_data['main']['temp'])+'C',
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
            "main": str(list_data ['weather'][0]['main']),
            "description": str(list_data['weather'][0]['description']),
            "icon" :str(list_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data = {}
    return render(req,"climate.html",data)