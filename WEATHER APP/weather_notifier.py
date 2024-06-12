import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, messagebox as mb
import requests
from plyer import notification
import time

# OpenWeather API keys
api_key = '16fe26b542aa77552cdc68a442e0c5e5'
geocode_base_url = "http://api.openweathermap.org/geo/1.0/direct?"
one_call_base_url = "https://api.openweathermap.org/data/3.0/onecall?"

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # Getting input of name of the place from user
    try:
        # Get coordinates from the city name
        geocode_url = f"{geocode_base_url}q={cityName}&appid={api_key}"
        print(f"Geocode URL: {geocode_url}")  # Debug print
        response = requests.get(geocode_url)
        location_data = response.json()
        print(f"Location data: {location_data}")  # Debug print
        
        if not location_data:
            mb.showerror('Error', 'City not found')
            return
        
        lat = location_data[0]['lat']
        lon = location_data[0]['lon']
        
        # Get weather data using the One Call API
        weather_url = f"{one_call_base_url}lat={lat}&lon={lon}&appid={api_key}"
        print(f"Weather URL: {weather_url}")  # Debug print
        response = requests.get(weather_url)
        weather_data = response.json()
        print(f"Weather data: {weather_data}")  # Debug print
        
        # Extracting relevant data
        temp = weather_data['current']['temp'] - 273.15  # Converting temperature from Kelvin to Celsius
        pres = weather_data['current']['pressure']
        hum = weather_data['current']['humidity']
        weather_desc = weather_data['current']['weather'][0]['description']
        
        # Combining the above values as a string 
        info = (
            f"Here is the weather description of {cityName}:"
            f"\nTemperature = {temp:.2f}°C"
            f"\nAtmospheric pressure = {pres} hPa"
            f"\nHumidity = {hum}%"
            f"\nDescription of the weather = {weather_desc}"
        )
        print(f"Weather info: {info}")  # Debug print

        # Showing the notification 
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            # Displaying time
            timeout=10
        )
        print("Notification sent")  # Debug print
        # Waiting time
        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error', str(e))  # Show pop-up message if any error occurred
        print(f"Error: {str(e)}")  # Debug print

# Creating the window
wn = tk.Tk()
wn.title("Python Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="Python Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the city name
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

# Run the window till the user closes it
wn.mainloop()



