import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    if all(field in animal for field in ["name", "characteristics"]):
        output += f"Name: {animal['name']}\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type'].capitalize()}\n"
        output += "\n"

new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as html_file:
    html_file.write(new_html_content)