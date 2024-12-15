import requests
import json


def fetch_data_from_api(api_url, api_key):
    """
    Holt Tierdaten von der API.

    Args:
        api_url (str): Die URL der API.
        api_key (str): Der API-Schlüssel.

    Returns:
        list: Liste von Tierobjekten.
    """
    headers = {'X-Api-Key': api_key}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        return []


def serialize_animal(animal):
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
    return ''.join(serialize_animal(animal) for animal in animals)


def main():
    api_key = 'FmI7ueh3zKOuD7vSMz/mHQ==0PPHN66Qsdo47uoj'

    # Benutzer nach dem Tiernamen fragen
    animal_name = input("Enter a name of an animal: ")

    # API-URL anpassen
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'

    # Daten von der API abrufen
    animals_data = fetch_data_from_api(api_url, api_key)

    # HTML für Tiere generieren
    animal_html = generate_animal_html(animals_data)

    # HTML-Vorlage lesen
    template_file_path = 'animals_template.html'
    output_file_path = 'animals.html'

    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()

    # Platzhalter durch generiertes HTML ersetzen
    final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_html)

    # Finales HTML in Datei schreiben
    with open(output_file_path, 'w') as final_file:
        final_file.write(final_html)

    print(f"Website was successfully generated to the file {output_file_path}.")


if __name__ == "__main__":
    main()
