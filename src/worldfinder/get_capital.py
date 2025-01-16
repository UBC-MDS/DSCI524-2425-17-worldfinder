from worldfinder._internals import load_data

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

    # Check input is a string
    if not isinstance(country, str):
        raise TypeError(
            f"Expected a string as input, instead received a'{type(country)}'"
            )
    

    # Check input is not an empty string
    if country == '':
        raise ValueError(
            'Country passed was an empty string'
        )
    
    sanitized_input = country.lower().strip()
     

    countries_df = load_data("countries.csv")
    country_df = countries_df[countries_df['Country'].str.lower() == sanitized_input]

    # Check country passed exists
    if country_df.empty:
        raise ValueError(
            'Country passed does not exist in our data. Please check your spelling or other variants of the country name'
        )
    
    capital = country_df.iloc[0]['Capital/Major City']

    return capital