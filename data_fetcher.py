import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    [
      {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
      },
      ...
    ]
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    print(response)
    if response.status_code == requests.codes.ok:
        animal_data = response.json()
        # filtered_animals = [animal for animal in animal_data if animal['name'] == animal_name]
        # print(filtered_animals)
        return animal_data
    else:
        print("Error:", response.status_code, response.text)
        return None
