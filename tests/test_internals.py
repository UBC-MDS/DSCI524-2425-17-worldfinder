import pytest
import pandas as pd
from worldfinder._internals import load_data
import os
from pathlib import Path


def test_load_data_functionality():
    """
    Test that the function returns the correct value
    """
    expected_df = pd.DataFrame(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],
        columns=['x', 'y', 'z']
    )

    repo_root = Path(__file__).resolve().parent.parent  # obtain absolute path to root of repo
    test_data_path = repo_root / "tests"  # Append path to the test folder
    dir_path = str(test_data_path)

    result = load_data(dir_path, "dummy_csv.csv")
    pd.testing.assert_frame_equal(result, expected_df)


def test_load_data_dir_path_non_string():
    """
    Check TypeError is raised when given a non-string value for dir_path
    """
    non_string = 123
    with pytest.raises(
        TypeError,
        match=(
            f"dir_path should be a string, instead got '{type(non_string)}'"
        )
    ):
        load_data(non_string, "dummy_csv.csv")


def test_load_data_csv_name_non_string():
    """
    Check TypeError is raised when given a non-string value for csv_name
    """
    non_string = 123
    with pytest.raises(
        TypeError,
        match=(
            f"csv_name should be a string, instead got '{type(non_string)}'"
        )
    ):
        load_data("tests", non_string)


def test_load_data_csv_name_not_csv():
    """
    Check ValueError is raised when given a csv_name that does not end in .csv
    """
    non_csv_name = "dummy_csv"
    with pytest.raises(
        ValueError,
        match='Provided csv_name does not end with .csv'
    ):
        load_data("tests", non_csv_name)


def test_load_data_bad_csv_path():
    """
    Check FileNotFoundError is raised when given a bad file path
    """
    bad_csv_name = "bad_path.csv"
    bad_path_dir = "incorrect_path"
    with pytest.raises(FileNotFoundError, match='File path does not exist'):
        load_data(bad_path_dir, bad_csv_name)

def test_empty_csv_name():
    """
    Check ValueError is raised when given an empty csv_name
    """
    empty_csv_name = ""
    with pytest.raises(
        ValueError,
        match = "csv_name cannot be an empty string"
    ):
        load_data("tests", empty_csv_name)

def test_empty_dir_path():
    """
    Check ValueError is raised when given an empty csv_name
    """
    dir_path = ""
    with pytest.raises(
        ValueError,
        match = "dir_path cannot be an empty string"
    ):
        load_data(dir_path, "dummy_csv.csv")
