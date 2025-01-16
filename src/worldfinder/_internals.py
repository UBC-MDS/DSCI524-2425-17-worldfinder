from importlib.resources import files
import pandas as pd


def load_data(csv_name):
    """
    Load data from the CSV file
    
    Parameters:
    -----------
    csv_name : str
        File name of the dataset to be loaded
    
    Returns:
    --------
    DataFrame
        A Pandas DataFrame containing the countries data

    Examples:
    ---------
    load_data("countries.csv")

    """
    csv_path = files("worldfinder.data").joinpath(csv_name)
    return pd.read_csv(csv_path)
