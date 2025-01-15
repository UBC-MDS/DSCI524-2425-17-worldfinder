import pytest
from worldfinder.get_country_statistic import get_country_statistic


def test_get_country_statistic_functionality():
    """
    Test that the function returns the correct value
    """
    result = get_country_statistic("Canada", "population")
    assert result == '36,991,981'


def test_get_country_statistic_case_insensitive():
    """
    Test that the function properly ignores case sensitivity
    """
    result_lower = get_country_statistic("canada", "population")
    result_upper = get_country_statistic("CANADA", "POPULATION")
    assert result_lower == result_upper


def test_get_country_statistic_different_data():
    """
    Test that the function doesn't just return the same value for all inputs
    """
    result_1 = get_country_statistic("Canada", "population")
    result_2 = get_country_statistic("United States", "population")
    assert result_1 != result_2


def test_get_country_statistic_country_non_string():
    """
    Check TypeError is raised when given a non-string value for country
    """
    non_string = 123
    with pytest.raises(TypeError, match=f"country should be a string, instead got '{type(non_string)}'"):
        get_country_statistic(non_string, "population")


def test_get_country_statistic_statistic_non_string():
    """
    Check TypeError is raised when given a non-string value for statistic
    """
    non_string = 123
    with pytest.raises(TypeError, match=f"statistic should be a string, instead got '{type(non_string)}'"):
        get_country_statistic("Canada", non_string)


def test_get_country_statistic_country_empty_string():
    """
    Check TypeError is raised when given a non-string value for statistic
    """
    empty_string = ""
    with pytest.raises(ValueError, match='country cannot be empty string'):
        get_country_statistic(empty_string, "population")


def test_get_country_statistic_statistic_empty_string():
    """
    Check TypeError is raised when given a non-string value for statistic
    """
    empty_string = ""
    with pytest.raises(ValueError, match='statistic cannot be empty string'):
        get_country_statistic("Canada", empty_string)


# def test_get_country_statistic_valid_statistic():
#     """
#     Check TypeError is raised when given a non-string value for statistic
#     """
#     empty_string = ""
#     with pytest.raises(ValueError, match='statistic cannot be empty string'):
#         get_country_statistic("Canada", empty_string)