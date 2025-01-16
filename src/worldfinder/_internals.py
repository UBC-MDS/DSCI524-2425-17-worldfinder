import pandas as pd
import os.path


def load_data(dir_path, csv_name):
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
    # Check that csv_name is a string
    if not isinstance(csv_name, str):
        raise TypeError(
            f"country should be a string, instead got '{type(csv_name)}'"
        )

    if not csv_name.endswith('.csv'):
        raise ValueError(
            'Provided csv_name does not end with .csv'
        )
    csv_path = os.path.join(dir_path, csv_name)

    # Check that file exists at file path
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(
            f"No file exists at {csv_path}"
        )

    return pd.read_csv(csv_path)
