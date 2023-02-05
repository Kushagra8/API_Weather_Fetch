# module for getting data from a website
import requests

# Current Weather API Key for OpenWeatherMap API
api_key = "aedeb5fdc56589e223a1b1d08144eb58"


# Function to retrieve weather data from OpenWeatherMap API
def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()


# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


# Main function to run the Api_Weather_Fetch
def weather_app(api_key):
    city = input("Enter your city name: ")
    weather_data = get_weather_data(api_key, city)
    if weather_data["cod"] != "404":
        temperature = kelvin_to_celsius(weather_data["main"]["temp"])
        print(f"The current temperature in {city} is {temperature:.2f}°C.")
    else:
        print("City not found.")


# Runs the script
if __name__ == '__main__':
    weather_app(api_key)
