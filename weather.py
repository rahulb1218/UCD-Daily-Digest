import requests
def getWeather():
    api_key = "API_KEY"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Woodland"
    complete_url = base_url + "appid=" + 'APP_ID' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        
        fahrenheit = (1.8 * (current_temperature - 273)) + 32
        round(fahrenheit)
        z = x["weather"]

        weather_description = z[0]["description"]

        return "Temperature: " + str(round(fahrenheit)) + " \N{DEGREE SIGN}F, Condition: " + str(weather_description)

    else:
        return " City Not Found "