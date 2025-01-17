import pandas as pd
import os.path


def load_data(dir_path, csv_name):
    """
    Load data from the CSV file.

    Parameters:
    -----------
    dir_path : str
        Path to directory containing the csv file

    csv_name : str
        File name of the dataset to be loaded

    Returns:
    --------
    DataFrame
        A Pandas DataFrame containing the csv data

    Raises:
    -------
    TypeError
        If dir_path or csv_name are not a string.

    ValueError
        If csv_name does not end with .csv.

    FileNotFoundError
        If the file at the specified path does not exist.

    Examples:
    ---------
    >>> df = load_data("src/worldfinder/data", "countries.csv")
    >>> df
    """

    # Check that csv_name is a string
    if not isinstance(csv_name, str):
        raise TypeError(
            f"csv_name should be a string, instead got '{type(csv_name)}'"
        )

    # Check that dir_path is a string
    if not isinstance(dir_path, str):
        raise TypeError(
            f"dir_path should be a string, instead got '{type(dir_path)}'"
        )

    # Check that csv_name ends with .csv
    if not csv_name.endswith('.csv'):
        raise ValueError(
            'Provided csv_name does not end with .csv'
        )
    csv_path = os.path.join(dir_path, csv_name)

    # Check that file exists at file path
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(
            'File path does not exist'
        )

    return pd.read_csv(csv_path)
