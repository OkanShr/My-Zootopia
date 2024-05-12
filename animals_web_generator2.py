import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    if all(field in animal for field in ["name", "locations", "characteristics"]):
      if "locations" in animal and "characteristics" in animal :
        if "diet" in animal["characteristics"] and "type" in animal["characteristics"]:
          print("Name:", animal["name"])
          print("Diet:", animal["characteristics"]["diet"])
          print("Location:", animal["locations"][0])
          print("Type:", animal["characteristics"]["type"])
          print()