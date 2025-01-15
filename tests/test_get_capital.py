from worldfinder.get_capital import get_capital

def test_capital_correct():
    """
    Test the correct capital is being returned
    """
    expected = "Rome"
    actual = get_capital('Italy')

    assert actual == expected