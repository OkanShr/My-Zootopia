import data_fetcher


def main():
    def serialize_animal(animal_obj):
        """Serializes a single animal object to HTML"""
        output = []
        output.append("<li class=\"cards__item\">")
        output.append(
            f"  <div class=\"card__title\">{animal_obj['name']}</div>")
        output.append("  <p class=\"card__text\">")
        output.append("    <ul class=\"animal-info\">")

        if "locations" in animal_obj and animal_obj["locations"]:
            output.append(
                f"<li>Location: {', '.join(animal_obj['locations'])}</li>")

        characteristics = animal_obj.get("characteristics", {})
        if "type" in characteristics:
            output.append(
                f"<li>Type: {characteristics['type'].capitalize()}</li>")
        if "diet" in characteristics:
            output.append(f"<li>Diet: {characteristics['diet']}</li>")

        output.append("    </ul>")
        output.append("  </p>")
        output.append("</li>")

        return "\n".join(output)

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

    new_html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as html_file:
        html_file.write(new_html_content)


if __name__ == "__main__":
    main()
