import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

animals_data = load_data('animals_data.json')


def generate_repository(animals):
    """ Generates the output for the animals and creates
        a new animals.html file replacing the
        __REPLACE_ANIMALS_INFO__ from animals_template.html
    """
    output = ""
    for animal in animals:
        if all(field in animal for field in ["name", "characteristics"]):
            output += "<li class=\"cards__item\">\n"
            output += f"  <div class=\"card__title\">{animal['name']}</div>\n"
            output += "  <p class=\"card__text\">\n"
            if "locations" in animal and animal["locations"]:
                output += f"      <strong>Location:</strong> {', '.join(animal['locations'])}<br/>\n"
            if "characteristics" in animal and "type" in animal["characteristics"]:
                output += f"      <strong>Type:</strong> {animal['characteristics']['type'].capitalize()}<br/>\n"
            if "characteristics" in animal and "diet" in animal["characteristics"]:
                output += f"      <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
            output += "  </p>\n"
            output += "</li>\n"

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as html_file:
        html_file.write(new_html_content)


generate_repository(animals_data)