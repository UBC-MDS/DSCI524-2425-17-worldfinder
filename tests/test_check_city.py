import pytest
from worldfinder.check_city import check_city

def test_type_error():
    """
    Test if function returns type error if type of input is incorrect
    """
    with pytest.raises(TypeError, match="City input must be a string."):
        check_city(123, "Nepal")

    with pytest.raises(TypeError, match="Country input must be a string."):
        check_city("Michigan", 45.6)

def test_value_error():
    """
    Test if function returns value error if value of input is incorrect
    """
    with pytest.raises(ValueError, match="Input city is not in database, please ensure correct spelling or try alternative names."):
        check_city("Stardew", "Nepal")

    with pytest.raises(ValueError, match="Input country is not in database, please ensure correct spelling or try alternative names."):
        check_city("Michigan", "Hyrule")

def test_empty_string_error():
    """
    Test if function returns value error if input is empty
    """
    with pytest.raises(ValueError, match="Input city cannot be an empty string"):
        check_city("", "Germany")
    with pytest.raises(ValueError, match="Input country cannot be an empty string"):
        check_city("Seoul", "")   

def test_return_results():
    """
    Test if it returns results correctly
    """
    assert check_city("London", "Canada") == True
    assert check_city("Vancouver", "China") == False
    assert check_city("London", "United Kingdom") == True

def test_case_sensitivity():
    """
    Test if it handles case sensitivity in input correctly
    """
    assert check_city("PARis", "France") == True
    assert check_city("Seattle", "UnitED staTEs") == True

def test_blank_space():
    """
    Test if it handles trailing blank spaces in input correctly
    """
    assert check_city(" Bangkok  ", "Thailand") == True
    assert check_city("Manila", "  Philippines  ") == True

 