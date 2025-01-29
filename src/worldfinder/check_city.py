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

    Examples
    -------
    >>> checkCity("London", "Canada")
    True
    '''
    if not isinstance(city, str):
        raise TypeError("City input must be a string.")
    
    if not isinstance(country, str):
        raise TypeError("Country input must be a string.")

    if city == '':
        raise ValueError(
            "Input city cannot be an empty string")
    
    if country == '':
        raise ValueError(
            "Input country cannot be an empty string")
            
    cities = load_data("data", "cities.csv")
    
    if not bool(cities["country_name"].str.lower().eq(country.strip().lower()).any()):
        raise ValueError("Input country is not in database, please ensure correct spelling or try alternative names.")

    if not bool(cities["name"].str.lower().eq(city.strip().lower()).any()):
        raise ValueError("Input city is not in database, please ensure correct spelling or try alternative names.")

    cities = cities[cities["country_name"].str.lower() == country.strip().lower()][[
        "name"]]
        
    return bool(cities["name"].str.lower().eq(city.strip().lower()).any())
