import os
import requests


def get_weather(city):
    api_key = os.environ.get("WEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        sky = data["weather"][0]["description"]
        return f"{city}: {temp}°C, {sky}"
    except requests.exceptions.RequestException as err:
        return f"Could not get weather: {err}"


if __name__ == "__main__":
    print(get_weather("Mumbai"))
