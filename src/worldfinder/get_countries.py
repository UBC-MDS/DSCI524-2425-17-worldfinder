from worldfinder._internals import load_data

def get_countries(city):
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
    >>> get_countries("London")
    ["Canada", "United Kingdom", "United States"]
    """

    # Check input is a string
    if not isinstance(city, str):
        raise TypeError(f"City should be a string, instead got '{type(city)}'")

    # Ensure 'city' is not empty
    if city.strip() == '':
        raise ValueError("City cannot be an empty string")

    # Load city data from CSV (replace with correct path/filename as needed)
    city_df = load_data("data", "cities.csv")

    # Check if the city exists in the dataset (case-insensitive)
    city_mask = city_df["name"].str.lower().eq(city.strip().lower())
    if not city_mask.any():
        raise ValueError(
            "City is not in the database. Please ensure correct spelling or try alternative names"
        )

    # Filter rows that match the given city (case-insensitive)
    matched_rows = city_df[city_mask]

    # Extract unique countries in their original case
    unique_countries = matched_rows["country_name"].unique().tolist()

    # Return the list of unique countries
    return unique_countries