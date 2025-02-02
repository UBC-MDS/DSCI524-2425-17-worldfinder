from worldfinder._internals import load_data


def get_country_statistic(country, statistic):
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
    string
        The value corresponding to the specified statistic for a specified
        country.

    Raises:
    -------
    TypeError
        If country or statistic are not a string.

    ValueError
        If country or statistic contain an empty string OR
        If statistic is not population, gdp, birth rate, cpi, or unemployment
        rate OR
        If country is not a valid country

    Examples
    -------
    >>> getCountryStatistic("Canada", "population")
    '36,991,981'
    '''

    # Check that country is a string
    if not isinstance(country, str):
        raise TypeError(
            f"country should be a string, instead got '{type(country)}'"
        )

    # Check that statistic is a string
    if not isinstance(statistic, str):
        raise TypeError(
            f"statistic should be a string, instead got '{type(statistic)}'"
        )

    # Check that country is not an empty string
    if country == '':
        raise ValueError(
            'country cannot be empty string'
            )

    # Check that statistic is not an empty string
    if statistic == '':
        raise ValueError(
            'statistic cannot be empty string'
            )

    stat_list = ["population", "gdp", "birth rate", "cpi", "unemployment rate"]

    # Check that statistic is a correct option
    if statistic.lower().strip() not in stat_list:
        raise ValueError(
            'statistic must be population, gdp, birth rate, cpi, or '
            'unemployment rate'
        )

    # Load country csv data in to dataframe
    country_df = load_data("data", "countries.csv")

    single_country_df = country_df[
        country_df["Country"].str.lower() == country.lower().strip()
    ]

    # Check that country exists in dataframe
    if single_country_df.empty:
        raise ValueError(
            f"country '{country}' is not a valid country name."
        )

    # Convert column names to lowercase
    single_country_df.columns = single_country_df.columns.str.lower()

    stat = single_country_df.iloc[0][statistic.lower().strip()]

    return stat
