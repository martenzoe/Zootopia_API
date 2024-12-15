import json


def load_data(file_path):
    """
    Lädt JSON-Daten aus einer Datei.

    Args:
        file_path (str): Pfad zur JSON-Datei.

    Returns:
        dict: Geladene JSON-Daten.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def serialize_animal(animal):
    """
    Serialisiert ein einzelnes Tierobjekt zu HTML.

    Args:
        animal (dict): Ein Tierobjekt mit Eigenschaften.

    Returns:
        str: HTML-Repräsentation des Tieres.
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
    Generiert HTML für alle Tiere.

    Args:
        animals (list): Liste von Tierobjekten.

    Returns:
        str: HTML-Repräsentation aller Tiere.
    """
    return ''.join(serialize_animal(animal) for animal in animals)


def main():
    """
    Hauptfunktion zur Orchestrierung des HTML-Generierungsprozesses.
    """
    json_file_path = 'animals_data.json'
    template_file_path = 'animals_template.html'
    output_file_path = 'animals.html'

    # Daten laden
    animals_data = load_data(json_file_path)

    # HTML für Tiere generieren
    animal_html = generate_animal_html(animals_data)

    # HTML-Vorlage lesen
    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()

    # Platzhalter durch generiertes HTML ersetzen
    final_html = template_content.replace('__REPLACE_ANIMALS_INFO__',
                                          animal_html)

    # Finales HTML in Datei schreiben
    with open(output_file_path, 'w') as final_file:
        final_file.write(final_html)

    print(f"HTML-Datei wurde erfolgreich erstellt: {output_file_path}")


if __name__ == "__main__":
    main()