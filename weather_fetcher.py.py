import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f'{base_url}q={city}&appid={api_key}&units=metric'
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]
        
        result_label.config(text=f'Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description}')
    else:
        result_label.config(text='City not found')

def close_app():
    root.destroy()  # Terminate the application

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")  # Set the window size

# Create and configure styles
style = ttk.Style()
style.configure("TButton", foreground="blue", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 14))

# Create labels and entry fields
city_label = ttk.Label(root, text="Enter the City:")
city_label.pack(pady=10)

city_entry = ttk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = ttk.Label(root, text="", wraplength=300)
result_label.pack()

# Add a "Close" button
close_button = ttk.Button(root, text="Close", command=close_app)
close_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()
