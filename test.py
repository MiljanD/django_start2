
import requests
import os
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}



def collect_city_data_by_name(city):
    api_route = os.getenv("GET_CITY_PATH")
    params = {
        "text": city
    }

    response = requests.get(api_route, params=params, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(f"Status: {response.status_code} - Error: {response.text}")

    data = response.json()
    return data["features"]


def extract_unique(city_data_list):
    processed_cities = set()
    unique_cities = []

    for city in city_data_list:
        matching_key = f"{city["properties"]["name"]}, {city["properties"]["country"]}"
        if matching_key in processed_cities:
            continue
        processed_cities.add(matching_key)
        unique_cities.append(city)
    return unique_cities

def show_cities_list(city_data_list):
    for idx, city in enumerate(city_data_list):
        print(f"{idx + 1}. {city["properties"]["name"]}, {city["properties"]["country"]}")

    user_choice = int(input("Choose city from the list:"))
    if user_choice < 1 or user_choice > len(city_data_list):
        raise ValueError(f"Selected choice is not valid option. Select from 1 - {len(city_data_list)}.")
    return user_choice - 1

def extract_coords(city_data_list, city_idx=0):
    if len(city_data_list) > 1:
        uniques = extract_unique(city_data_list)
        city_idx = show_cities_list(uniques)
        return city_data_list[city_idx]["geometry"]["coordinates"]
    return city_data_list[city_idx]["geometry"]["coordinates"]


def get_distance_by_coords(origin, destination):
    api_route = os.getenv("GET_COORDS_PATH")

    body = {
        "locations": [origin, destination],
        "metrics": ["distance", "duration"]
    }

    response = requests.post(api_route, json=body, headers=headers)

    data = response.json()
    return round(data["distances"][0][1] / 1000, 2)



if __name__ == "__main__":
    city_from = collect_city_data_by_name("belgrade")
    city_to = collect_city_data_by_name("nis")
    origin_coords = extract_coords(city_from)
    destination_cords = extract_coords(city_to)
    distance = get_distance_by_coords(origin_coords, destination_cords)
    print(distance)