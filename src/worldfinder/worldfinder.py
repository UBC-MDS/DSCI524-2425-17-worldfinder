from importlib.resources import files
import pandas as pd


def load_countries_data():
    """
    Load the countries data from the CSV file

    Returns:
    --------
    DataFrame
        A Pandas DataFrame containing the countries data

    Examples:
    ---------
    load_countries_data()

    """
    csv_path = files("worldfinder.data").joinpath("countries.csv")
    return pd.read_csv(csv_path)

def load_cities_data():
    """
    Load the cities data from the CSV file.

    Returns:
    --------
    DataFrame
        A Pandas DataFrame containing the cities data

    Examples:
    ---------
    load_cities_data()

    """
    csv_path = files("worldfinder.data").joinpath("cities.csv")
    return pd.read_csv(csv_path)


def getCapital(country):
    """
    Retrieve the capital city of a given country.

    Parameters:
    -----------
    country : str
        The country in which the user wishes to find the capital city
    
    Returns:
    --------
    str
        The capital city corresponding to the country passed
    
    Examples:
    ---------
    getCapital("Italy")
    'Rome'
    """
    pass

def getCountries(city):
    """
    Return all unique countries that contain a given city.

    Parameters
    ----------
    city : str
        The name of the city to search for.

    Returns
    -------
    list of str
        A list of unique countries (in their original case) that contain the 
        specified city. The list will be deduplicated.

    Examples
    --------
    >>> getCountries("London")
    ["Canada", "England", "United States", "Australia", "South Africa", "Jamaica"]
    """
    pass

def checkCity(city, country):
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
    pass

def getCountryStatistic(country, statistic):
    '''
    Returns an integer or float representing a specific piece of 
    information about a country. Possible statistics include population, GDP,
    and surface area.

    Parameters
    ----------
    country: str
        The name of a country
    statistic: str
        The name of the statistic of interest

    Returns
    -------
    integer or float
        The value corresponding to the specified statistic for a specified country.

    Examples
    -------
    >>> getCountryStatistic("Canada", "population")
    41465298
    '''
    pass