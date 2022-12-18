import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')
API_KEY = os.getenv('OPENWEATHER_API_KEY')


def get_data(place, forecast_dasy=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    # Obtenemos 8 valores cada 24 horas. Como el máximo son 5 días tenemos como mucho 40 valores.
    nr_values = 8 * forecast_dasy
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Madrid", forecast_dasy=3, kind="Temperature"))
