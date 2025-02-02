from worldfinder.get_capital import get_capital
import pytest

def test_get_capital_correct():
    """
    Test the correct capital is being returned when an input is a string, not empty, and the country exists
    """
    expected = "Rome"
    actual = get_capital('Italy')

    assert actual == expected

def test_get_capital_input_type_error():
    """
    Test non string inputs throws an error
    """
    with pytest.raises(TypeError, match='Expected a string as input, instead received a'):
        get_capital(12)

def test_get_capital_input_empty_string():
    """
    Test empty string inputs throws an error
    """

    with pytest.raises(ValueError, match='Country passed was an empty string'):
        get_capital("")

def test_get_capital_case_insensitive_inputs():
    """
    Test that the string inputs work in upper/lower/mixed case
    """

    expected = 'Rome'
    actual_upper = get_capital('ITALY')
    actual_lower = get_capital('italy')
    actual_mixed = get_capital('iTaLy')

    assert expected == actual_upper == actual_lower == actual_mixed

def test_get_capital_variants_of_country_name():
    """
    Test that other forms of the country name should fail
    """

    with pytest.raises(ValueError, match='Country passed does not exist in our data. Please check your spelling or other variants of the country name'):
        get_capital('USA')

def test_get_capital_non_country_passed():
    """
    Test that a non-existent country should fail
    """
    with pytest.raises(ValueError, match='Country passed does not exist in our data. Please check your spelling or other variants of the country name'):
        get_capital('Portlandia')

def test_get_capital_trailing_and_leading_whitespace():
    """
    Test that trailing and leading whitespaces 
    """

    expected = 'Tokyo'
    actual = get_capital(' Japan   ')

    assert expected == actual

def test_get_capital_multiple_capitals():
    """
    Test that in the case of countries with multiple capitals, at least one is returned
    """

    expected = ["Pretoria", "Cape Town"]

    actual = get_capital('South Africa')

    assert actual in expected

def test_capital_not_returned():
    """
    Test that the function fails gracefully when a capital is not returned
    """

    with pytest.raises(ValueError, match = 'Country was found but the capital was not found.'):
        get_capital("Singapore")


