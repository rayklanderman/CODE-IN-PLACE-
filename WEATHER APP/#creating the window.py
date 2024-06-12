import tkinter as tk
from tkinter import StringVar, Label, Entry, Button, messagebox as mb
import requests
from plyer import notification
import time

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # Getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # Base URL from where we extract weather report
    try:
        # This is the complete URL to get weather conditions of a city
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)  # Requesting for the content of the URL
        x = response.json()  # Converting it into JSON
        y = x["main"]  # Getting the "main" key from the JSON object
 
        # Getting the "temp" key of y
        temp = y["temp"]
        temp -= 273  # Converting temperature from Kelvin to Celsius

        # Storing the value of the "pressure" key of y
        pres = y["pressure"]

        # Getting the value of the "humidity" key of y
        hum = y["humidity"]

        # Storing the value of "weather" key in variable z
        z = x["weather"]

        # Getting the corresponding "description"
        weather_desc = z[0]["description"]

        # Combining the above values as a string 
        info = (
            "Here is the weather description of " + cityName + ":"
            "\nTemperature = " + str(temp) + "°C"
            "\nAtmospheric pressure = " + str(pres) + "hPa"
            "\nHumidity = " + str(hum) + "%"
            "\nDescription of the weather = " + str(weather_desc)
        )

        # Showing the notification 
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            # Displaying time
            timeout=10
        )
        # Waiting time
        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error', e)  # Show pop-up message if any error occurred

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

