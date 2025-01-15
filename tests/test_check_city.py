import pytest
from worldfinder.check_city import check_city

def test_return_true():
    """
    Test if it returns True correctly
    """
    assert check_city("London", "Canada") == True

def test_return_false():
    """
    Test if it returns False correctly
    """
    assert check_city("Vancouver", "China") == False

def test_city_case_sensitivity():
    """
    Test if it handles case sensitivity in city input correctly
    """
    assert check_city("PARis", "France") == True

def test_country_case_sensitivity():
    """
    Test if it handles case sensitivity in country input correctly
    """
    assert check_city("Seattle", "UnitED staTEs") == True

