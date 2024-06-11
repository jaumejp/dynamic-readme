# Libraries:
import requests
from datetime import date, datetime
import random
import os

# Custom modules
from helpers.config import LANG_ID

# Get information of current day:
def get_current_day_name(DAYS):
    # Get the current day of the week (0 for Monday, 1 for Tuesday, etc.) and return its translated name.
    return DAYS[datetime.now().weekday()]

# Get temperature from weather:
def get_temp_max_from(city):
    """
    Gets the maximum temperature for a given city from the weather API.

    Args:
        city (str): The city for which to get the weather data.

    Returns:
        float: The maximum temperature for the specified city.
    """

    # Base url from the api
    base_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

    # If we don't have api key, return None
    try:
        API_KEY = os.environ['API_KEY']
    except KeyError:
        print("api key error")
        return None

    # Get today's date in the required format
    today = date.today().strftime('%Y-%m-%d')

    # Construct the endpoint URL
    endpoint = f"{base_url}/{city}/{today}/{today}"

    # Define the parameters for the request
    unit_group = 'metric'
    content_type = 'json'
    include = 'hours'

    params = {
        'unitGroup': unit_group,
        'key': API_KEY,
        'contentType': content_type,
        'include': include
    }

    try:
        # Make the GET request to the weather API
        response = requests.get(endpoint, params=params)

        # Check if the response status code is 200 (OK)
        response.raise_for_status()

        # Parse the JSON response
        weather_data = response.json()

        # Extract the maximum temperature from the response
        if 'days' in weather_data and len(weather_data['days']) > 0:
            return weather_data['days'][0].get('tempmax', None)
        else:
            print("No weather data available for the specified city and date.")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred during the request: {req_err}")
    except KeyError as key_err:
        print(f"Unexpected response format: missing key {key_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    return None

def shuffle_dictionary(d):
    """
    This function takes a dictionary and shuffles its key-value pairs randomly.
    
    Parameters:
    d (dict): The dictionary to be shuffled.
    
    Returns:
    dict: A new dictionary with the key-value pairs shuffled.
    """

    items = list(d.items())
    random.shuffle(items)

    return dict(items)

__all__ = ['get_current_day_name', 'get_temp_max_from', 'shuffle_dictionary']
