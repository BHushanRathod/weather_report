import json
import requests
from cities import CITY_DICT, API_KEYS

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"


def get_by_altitute():
    """
    Method to read the lat, long manually
    :return:
    """
    try:
        lat, long = input("Enter Lat and Long of a place: ").split()
        return lat, long
    except ValueError:
        print("Error while getting values.")
        get_by_altitute()


def get_by_city():
    """
    Method reads the city dict, displays names of the famous cities
    :return:
    """
    while True:
        try:
            for key in CITY_DICT:
                print(key)
            city = input("Enter city name: ")
            lat, long = CITY_DICT.get(city.capitalize())
            return lat, long
        except TypeError:
            print("~" * 50)
            print("Please enter the city name correctly")


def get_weather_report():
    """
    Method will use openweather API, provide Lat, Long and API_KEY
    :return:
    """
    try:
        lat, long = None, None
        option = input("Get weather report of City \n1.Select from database \n2.Enter manually\n")
        if option == '1':
            lat, long = get_by_city()
        elif option == '2':
            lat, long = get_by_altitute()
        print("~~~~~~~~~~~~~~~~~~~~~~~Getting the weather report for the city~~~~~~~~~~~~~~~~~~~~")
        response = requests.get(BASE_URL.format(lat, long, API_KEYS), verify=True)
        print(json.dumps(json.loads(response.text), indent=4))
    except ValueError:
        print("Select correct option.")


if __name__ == '__main__':
    get_weather_report()
