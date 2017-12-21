import requests
from pprint import pprint
def main():
    city = "Delhi"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=87372ade475bf9d25131cf2e87123660")
    weather =  response.json()
    pprint(weather)
    print(weather['main']['temp'])
    print("Weather for ", weather['name'])
    print(weather['weather'][0]['description'])
if __name__ == '__main__':
    main()