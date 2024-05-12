import data_fetcher


def serialize_animal(animal_obj):
    """Serializes a single animal object to HTML"""
    output = ""
    output += "<li class=\"cards__item\">\n"
    output += f"  <div class=\"card__title\">{animal_obj['name']}</div>\n"
    output += "  <p class=\"card__text\">\n"
    output += "    <ul class=\"animal-info\">\n"
    if "locations" in animal_obj and animal_obj["locations"]:
        output += f"      <li>Location: {', '.join(animal_obj['locations'])}</li>\n"
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        output += f"      <li>Type: {animal_obj['characteristics']['type'].capitalize()}</li>\n"
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        output += f"      <li>Diet: {animal_obj['characteristics']['diet']}</li>\n"
    output += "    </ul>\n"
    output += "  </p>\n"  # Added closing p tag
    output += "</li>\n"
    return output


animal_name = input("Please enter an animal: ")

data = data_fetcher.fetch_data(animal_name)
found = data is not None
output = ""

if found:
    output = ""
    for animal in data:
        output += serialize_animal(animal)
else:
    output = f"<h2>The animal {animal_name} doesn't exist.</h2>"

with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as html_file:
    html_file.write(new_html_content)
