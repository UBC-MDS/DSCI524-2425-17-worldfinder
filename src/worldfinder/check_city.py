import pandas as pd
from worldfinder._internals import load_data

def check_city(city, country):
    '''
    Returns boolean on whether a given city is present in the given country

    Parameters
    ----------
    city: str
        The name of a city
    country: str
        The name of a country

    Returns
    -------
    boolean
        True if the given city name is a city in the given country

    Raises:
    -------
    TypeError
        If city or country are not a string.

    ValueError
        If city or country contain an empty string OR
        If city is not a valid city OR
        If country is not a valid country
    
    Examples
    -------
    >>> checkCity("London", "Canada")
    True
    '''
    # Check that the city input is a string
    if not isinstance(city, str):
        raise TypeError("City input must be a string.")
    
    # Check that the country input is a string
    if not isinstance(country, str):
        raise TypeError("Country input must be a string.")

    # Check that the city input is not an empty string
    if city == '':
        raise ValueError(
            "Input city cannot be an empty string")
    
    # Check that the country input is not an empty string
    if country == '':
        raise ValueError(
            "Input country cannot be an empty string")
            
    # Load cities dataset
    cities = load_data("data", "cities.csv")
    
    # Check that city input is a valid city
    if not bool(cities["country_name"].str.lower().eq(country.strip().lower()).any()):
        raise ValueError("Input country is not in database, please ensure correct spelling or try alternative names.")

    # check that country input is a valid country
    if not bool(cities["name"].str.lower().eq(city.strip().lower()).any()):
        raise ValueError("Input city is not in database, please ensure correct spelling or try alternative names.")

    # Filter for list of cities in specified country only
    cities = cities[cities["country_name"].str.lower() == country.strip().lower()][[
        "name"]]
        
    return bool(cities["name"].str.lower().eq(city.strip().lower()).any())
