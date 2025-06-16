import requests

def weather(city):  # we can take the data from website 
    api_key = "6bc074ce5ba568bb12e6f7743a12deee"  # unique api key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # collecting data from website
    response = requests.get(url)
    print(response)

    # Convert the response into Python dictionary(json)
    data = response.json()
    print(data)
    
    if response.status_code == 200:
        print(f"\nWeather in {city.title()}:")
        print("Temperature:", data["main"]["temp"], "°C")
        print("Condition:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("City not found.")

# Call the function
w = weather("Madanapalle")
