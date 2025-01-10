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