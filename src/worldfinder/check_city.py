import pandas as pd
from worldfinder._internals import load_cities_data

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
    if not isinstance(cities, str):
        raise TypeError("City input must be a string.")
    
    if not isinstance(country, str):
        raise TypeError("Country input must be a string.")
    
    

    cities = load_cities_data()
    cities = cities[cities["country_name"].str.lower() == country.lower()][[
        "name"]]
        
    return bool(cities["name"].str.lower().eq(city.lower()).any())
