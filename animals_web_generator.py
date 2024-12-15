import requests
import data_fetcher
import json


def serialize_animal(animal):
    """
    Serializes a single animal object to HTML.

    Args:
        animal (dict): An animal object with properties.

    Returns:
        str: HTML representation of the animal.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name", "")}</div>\n'
    output += '  <p class="card__text">\n'

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += (f'      <strong>Diet:</strong> '
                   f'{animal["characteristics"]["diet"]}<br/>\n')

    if 'locations' in animal and animal['locations']:
        output += (f'      <strong>Location:</strong> '
                   f'{animal["locations"][0]}<br/>\n')

    if 'characteristics' in animal and 'type' in animal['characteristics']:
        output += (f'      <strong>Type:</strong> '
                   f'{animal["characteristics"]["type"]}<br/>\n')

    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animal_html(animals):
    """
    Generates HTML for all animals.

    Args:
        animals (list): A list of animal objects.

    Returns:
        str: HTML representation of all animals.
    """
    return ''.join(serialize_animal(animal) for animal in animals)


def main():
    # Ask the user for the name of the animal
    animal_name = input("Enter a name of an animal: ")

    # Fetch data from the API via data_fetcher
    animals_data = data_fetcher.fetch_data(animal_name)

    # Read the HTML template
    template_file_path = 'animals_template.html'
    output_file_path = 'animals.html'

    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()

    if animals_data:
        # Generate HTML for animals
        animal_html = generate_animal_html(animals_data)

        # Replace placeholder with generated HTML
        final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_html)
    else:
        # Message for non-existent animal
        final_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    # Write final HTML to file
    with open(output_file_path, 'w') as final_file:
        final_file.write(final_html)

    print(f"Website was successfully generated to the file {output_file_path}.")


if __name__ == "__main__":
    main()
