import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment variables
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetches the animals data for the specified animal name.

    Args:
        animal_name (str): The name of the animal to fetch data for.

    Returns:
        list: A list of animals, each represented as a dictionary.
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        'X-Api-Key': API_KEY,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the HTTP status code indicates success
        return response.json()  # Return the JSON data as a dictionary
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []  # Return an empty list if an error occurs
