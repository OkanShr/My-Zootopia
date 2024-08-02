import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """Reads and returns the content of the HTML template file."""
    with open(file_path, "r") as template_file:
        return template_file.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object to HTML."""
    output = "<li class=\"cards__item\">\n"
    output += f"  <div class=\"card__title\">{animal_obj['name']}</div>\n"
    output += "  <p class=\"card__text\">\n"
    output += "    <ul class=\"animal-info\">\n"
    if "locations" in animal_obj and animal_obj["locations"]:
        output += (f"<li>"
                   f"Location: {', '.join(animal_obj['locations'])}"
                   f"</li>\n")
    if ("characteristics" in animal_obj and "type"
            in animal_obj["characteristics"]):
        output += (f"<li>"
                   f"Type:{animal_obj['characteristics']['type'].capitalize()}"
                   f"</li>\n")
    if ("characteristics" in animal_obj and "diet"
            in animal_obj["characteristics"]):
        output += (f"      <li>"
                   f"Diet: {animal_obj['characteristics']['diet']}"
                   f"</li>\n")
    output += "    </ul>\n"
    output += "  </p>\n"
    output += "</li>\n"
    return output


def get_available_skin_types(animals):
    """Returns a set of available skin types."""
    skin_types = set()
    for animal in animals:
        if ("characteristics" in animal and "skin_type"
                in animal["characteristics"]):
            skin_types.add(animal["characteristics"]["skin_type"])
    return skin_types


def main():
    template_content = read_template("animals_template.html")
    animals_data = load_data('animals_data.json')

    available_skin_types = get_available_skin_types(animals_data)

    print("Available skin types:")
    for skin_type in available_skin_types:
        print(skin_type)

    selected_skin_type = input("Enter a skin type from the list above: ")

    output = ""
    for animal_data in animals_data:
        if ("characteristics" in animal_data and "skin_type"
                in animal_data["characteristics"]):
            if (animal_data["characteristics"]["skin_type"]
                    == selected_skin_type):
                output += serialize_animal(animal_data)
        elif "characteristics" not in animal_data:
            output += serialize_animal(animal_data)

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as html_file:
        html_file.write(new_html_content)


if __name__ == "__main__":
    main()
