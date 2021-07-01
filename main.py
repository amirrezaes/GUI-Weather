# coded by amirreza.es
# weather script
# online service: https://www.apixu.com
import requests
import json
from tkinter import *

root = Tk()
root.geometry("600x500+30+30")
root.configure(background='medium aquamarine')


#########################

def connect():

    global parsed_json
    
    try:

        f = requests.get('http://api.weatherstack.com/current?access_key=<put your key here>&query=' + str(entry.get())+'&units=m')
        parsed_json = json.loads(f.text)
    except:
        
        label = Label(root, text="Check your connection and City name.",bg='black', fg='red', font='15').pack()

    city = parsed_json ['location']['name']
    weather = parsed_json['current']['weather_descriptions'][0]
    temperature = parsed_json['current']['temperature']
    feelslike = parsed_json['current']['feelslike']
    last_up = parsed_json['current']['observation_time']
    windSpeed = parsed_json['current']['wind_speed']
    humidity = parsed_json['current']['humidity']
    cloud = parsed_json['current']['cloudcover']
    precip_mm = parsed_json['current']['precip']
    city1 = 'City: ' + str(city)
    weather1 = 'Condition: ' + weather
    temperature1 = 'Temperature: ' + str(temperature) + ' C'
    feelslike1 = 'Feels like: ' + str(feelslike) + ' C'
    windSpeed1 = 'Wind speed: ' + str(windSpeed) + '/Kmph'
    cloud1 = 'Cloud: ' + str(cloud) + ' %'
    humidity1 = 'Humidity: ' + str(humidity) + ' %'
    precipitation = 'Precipitation: ' + str(precip_mm) + ' mm'
    last_up1 = 'Last update time: ' + str(last_up)

    label = Label(root, text=
    city1 + '\n' + weather1 + '\n' + temperature1 + '\n' +
    feelslike1 + '\n' + windSpeed1 + '\n' + cloud1 + '\n' + humidity1
    + '\n' + precipitation + '\n' + last_up1, bg='medium aquamarine', fg='red', font='13').pack()

# ==============================================================================================

but = Button(root, text='Show the weather', width=20, bg="PeachPuff3", command=connect)
entry = Entry(root, width=46)
entry.insert(END, "")
entry.pack(side='top')
but.pack(side='top')

root.mainloop()
