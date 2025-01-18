from worldfinder.get_countries import get_countries
import pytest

def test_get_countries_non_string():
    """
    Test if the input is a non-string value
    """
    with pytest.raises(TypeError, match=f"City should be a string, instead got '{type(88)}'"):
        get_countries(88)

def test_get_countries_empty_string():
    """
    Test if the input is an empty string
    """
    with pytest.raises(ValueError, match='City cannot be an empty string'):
        get_countries("")

def test_get_countries_wrong_input():
    """
    Test if the input is not in database
    """
    with pytest.raises(ValueError, match="City is not in the database. Please ensure correct spelling or try alternative names"):
        get_countries("Adco")

def test_get_countries_case_insensitivity():
    """
    Test if function behaves the same regardless of the case
    used to pass the city name.
    """
    city_lowercase = get_countries("london")
    city_uppercase = get_countries("London")
    city_mixed = get_countries("LoNDon")
    city_capital = get_countries("LONDON")
    assert city_lowercase == city_uppercase == city_mixed == city_capital, (
        f"Expected the same result for 'London', 'london', 'LoNDon', 'LONDON'"
    )

def test_get_countries_trailing_whitespace():
    """
    Test if function handles leading/trailing whitespace correctly.
    """
    city_no_whitespace = get_countries("London")
    city_with_whitespace = get_countries("  London  ")
    assert city_no_whitespace == city_with_whitespace, (
        "Expected the same result for 'London' and '  London  '"
    )

def test_get_countries_returns_expected_countries():
    """
    Test if function returns the correct list of countries for a known city.
    """
    city = "London"
    expected_countries = ["Canada", "United Kingdom", "United States"]
    
    result = get_countries(city)

    # Check that 'result' is a list
    assert isinstance(result, list), "Expected a list of countries, but got something else."

    # Check that the result is not empty
    assert len(result) > 0, f"Expected at least one country for city '{city}', but got none."

    # Check that each expected country is in the result
    for country in expected_countries:
        assert country in result, (
            f"Expected country '{country}' to be in the result for city '{city}', "
            f"but it was not found. Result: {result}"
        )

def test_get_countries_returns_unique_values():
    """
    Test that the list returned by get_countries contains only unique values.
    """
    city = "London"
    result = get_countries(city)

    # Ensure the result is a list
    assert isinstance(result, list), f"Expected a list, but got {type(result)}"

    # Check that the length of the list matches the length of the set of the list
    # If there are duplicates, these lengths would not match.
    assert len(result) == len(set(result)), (
        f"Expected unique country values, but found duplicates in {result}"
    )
        