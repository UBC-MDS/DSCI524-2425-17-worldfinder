import pytest
from worldfinder.check_city import check_city

def test_type_error():
    """
    Test if function returns type error if type of input is incorrect.
    """

    with pytest.raises(TypeError, match="City input must be a string."):
        check_city(123, "Nepal")    # Testing for when the city input is not a string

    with pytest.raises(TypeError, match="Country input must be a string."):
        check_city("Michigan", 45.6) # Testing for when country input is not a string

def test_value_error():
    """
    Test if function returns value error if value of input is incorrect
    """
    with pytest.raises(ValueError, match="Input city is not in database, please ensure correct spelling or try alternative names."):
        check_city("Stardew", "Nepal") # Testing for when city is not in the database

    with pytest.raises(ValueError, match="Input country is not in database, please ensure correct spelling or try alternative names."):
        check_city("Michigan", "Hyrule") # Testing for when country is not in the database

def test_empty_string_error():
    """
    Test if function returns value error if input is empty
    """
    with pytest.raises(ValueError, match="Input city cannot be an empty string"):
        check_city("", "Germany") # Testing for when there is empty string in city input
    with pytest.raises(ValueError, match="Input country cannot be an empty string"):
        check_city("Seoul", "")   # Testing for when there is empty string in country input

def test_return_results():
    """
    Test if it returns results correctly
    """
    assert check_city("London", "Canada") == True  # Testing for when given city is in given country
    assert check_city("Vancouver", "China") == False # Testing for when given city is not in given country
    assert check_city("London", "United Kingdom") == True # Testing for when a given city has multiple matching countries

def test_case_sensitivity():
    """
    Test if it handles case sensitivity in input correctly
    """
    assert check_city("PARis", "France") == True # Testing for case sensitivity in city input
    assert check_city("Seattle", "UnitED staTEs") == True # Testing for case sensitivity in country input

def test_blank_space():
    """
    Test if it handles trailing blank spaces in input correctly
    """
    assert check_city(" Bangkok  ", "Thailand") == True # Testing for trailing blank spaces in city input
    assert check_city("Manila", "  Philippines  ") == True # Testing for trailing blank spaces in country input

 