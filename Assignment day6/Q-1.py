import requests

# f = format string
def weather_data(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b6c2fa62e9b39df97a129a448fe44520&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print( f"Temp : {data['main']['temp']}°C")
        print(f"Pressure : {data['main']['pressure']}")
        print(f"Feels Like : {data['main']['feels_like']}°C")
        print(f"Temp Min : {data['main']['temp_min']}°C")
        print(f"Temp Max : {data['main']['temp_max']}°C")
        print(f"Humidity : {data['main']['humidity']}")
        print(f"Sea Level : {data['main'].get('sea_level', 'Not Available')}")
        print(f"Ground Level : {data['main'].get('grnd_level', 'Not Available')}")
        

    except requests.exceptions.RequestException as e:
        print(e)

city = input("Enter the city name : ")
weather_data(city)