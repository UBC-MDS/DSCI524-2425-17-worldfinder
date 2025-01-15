from worldfinder._internals import load_countries_data, load_cities_data

def get_capital(country):
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
    get_capital("Italy")
    'Rome'
    """
    # Checking parameters passed
    if not isinstance(country, str):
        raise TypeError(
            f"Expected a string as input, instead received a'{type(country)}'"
            )
    
    if country == '':
        raise ValueError(
            'Country passed was an empty string'
        )
    
    
    countries_df = load_countries_data()
    country_df = countries_df[countries_df['Country'].str.lower() == country.lower()]

    if country_df.empty:
        return 
    
    capital = country_df.iloc[0]['Capital/Major City']
    return capital