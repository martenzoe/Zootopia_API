import requests

API_KEY = 'FmI7ueh3zKOuD7vSMz/mHQ==0PPHN66Qsdo47uoj'
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Args:
        animal_name (str): The name of the animal to fetch data for.

    Returns:
        list: A list of animals, each represented as a dictionary.
    """
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f'{API_URL}?name={animal_name}', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        return []
