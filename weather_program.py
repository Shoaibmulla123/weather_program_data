import requests

def get_weather_data():
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def get_temperature_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['temp']
    return None

def get_wind_speed_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['wind']['speed']
    return None

def get_pressure_by_date(data, date):
    for item in data['list']:
        if item['dt_txt'].startswith(date):
            return item['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD format): ")
            temperature = get_temperature_by_date(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} °C")
            else:
                print("Weather data not available for the specified date.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD format): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Wind Speed data not available for the specified date.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD format): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Pressure data not available for the specified date.")

        elif choice == '0':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
