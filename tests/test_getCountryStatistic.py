import pytest
from worldfinder.worldfinder import getCountryStatistic


def test_getCountryStatistic_functionality():
    """
    Test that the function returns the correct value
    """
    result = getCountryStatistic("Canada", "population")
    assert result == '36,991,981'


def test_getCountryStatistic_case_insensitive():
    """
    Test that the function properly ignores case sensitivity
    """
    result_lower = getCountryStatistic("canada", "population")
    result_upper = getCountryStatistic("CANADA", "POPULATION")

    assert result_lower == result_upper


def test_getCountryStatistic_country_non_string():
    """
    Check TypeError is raised when given a non-string value for country
    """
    with pytest.raises(TypeError, match="country must be a string"):
        getCountryStatistic(123, "population")


def test_getCountryStatistic_statistic_non_string():
    """
    Check TypeError is raised when given a non-string value for statistic
    """
    with pytest.raises(TypeError, match="country must be a string"):
        getCountryStatistic("Canada", 123)