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