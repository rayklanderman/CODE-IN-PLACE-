## **Weather Notification App**

**Overview**

This Python-based desktop application delivers real-time weather updates directly to your desktop. It utilizes the OpenWeather API to fetch weather data and leverages the Plyer library to display informative notifications.

**Features**

* **Personalized Weather:** Get accurate weather information tailored to your specific location.
* **Instant Notifications:** Receive timely weather alerts without opening any additional apps.
* **User-Friendly Interface:** Easily input your location and retrieve weather data with a simple click.

**Usage**

1. **Run the Application:** Execute the Python script to launch the app.
2. **Enter Location:** Input your desired location in the provided field.
3. **Get Notification:** Click the "Get Notification" button to retrieve and display the weather information.

**Technical Details**

* **OpenWeather API:** Fetches weather data using the OpenWeather API.
* **Plyer Library:** Displays notifications in a visually appealing manner.
* **Tkinter Library:** Creates a user-friendly graphical interface.
* **getNotification Function:** Retrieves weather data and presents it in a notification.

**API Keys**

To use this app, you'll need an OpenWeather API key. Replace the `api_key` variable with your own key.

**Code Structure**

```python
import requests
from tkinter import *
from plyer import notification

def getNotification():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = round(data["main"]["temp"] - 273.15, 2)
        description = data["weather"][0]["description"]
        notification.notify(
            title=f"Weather in {city}",
            message=f"Temperature: {temperature}°C\n{description}",
            app_icon="path/to/your/app/icon.ico",  # Optional: Add an app icon
            timeout=10  # Notification timeout in seconds
        )
    else:
        print("Error fetching weather data.")

# Create the GUI
root = Tk()
root.title("Weather Notification App")

city_label = Label(root, text="Enter City:")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

get_button = Button(root, text="Get Notification", command=getNotification)
get_button.pack()

root.mainloop()
```

**Troubleshooting**

* **API Key:** Ensure you've replaced the placeholder API key with your own.
* **Internet Connection:** Verify that you have a stable internet connection.
* **Error Messages:** Check the console for any error messages and debug accordingly.

**Enjoy your personalized weather notifications!** ☀️🌧️❄️
