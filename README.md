# worldfinder

[![Documentation Status](https://readthedocs.org/projects/worldfinder/badge/?version=latest)](https://worldfinder.readthedocs.io/en/latest/?badge=latest)

This packages provides a set of four functions for working with geographical information about cities and countries. These functions will allow users to find the capital city of a country, find all countries that contain a given city name, determine if a city belongs to a specific country, and get statistics about a specified country such as population, GDP, and surface area. These functions will utilize a pre-existing database of city and country information to return the necessary information.

## Functions and Data

### Data
The data for this library will come from two csv files containing country and city information.

- cities.csv: Contains information about cities around the world. Data was retrieved from Darshan Gada's GitHub repository [here](https://github.com/dr5hn/countries-states-cities-database).
- countries.csv: Contains information about countries around the world. Data was retrieved from Nidula Elgiriyewithana's Kaggle dataset [here](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023).

### Functions
- `get_capital(country)`:
    - This function will retrieve the capital city of a given country name passed as an input. The function outputs a string representing the capital city name.

- `get_countries(city)`:
    - This function searches for a specified city and returns a list of strings of unique countries where the city is located.

- `check_city(city, country)`:
    - This function will return a boolean on if the given city exist in the given country. It will return True if the city exists in a given country otherwise it will return False.

- `get_country_statistic(country, statistic)`:
    - This function will return a string representing a specified statistic for a given country.

## worldfinder in the Python Ecosystem
The PyPI server hosts numerous packages related to country and city data. Among these, we have identified a few noteworthy examples that offer functionality similar to our package. For instance, a package with functionality similar to our `get_capital` function can be found [here](https://pypi.org/project/country-capitals/). Similarly, a package providing features comparable to our `get_country_statistics` function, which retrieves information about a specified country, is available [here](https://pypi.org/project/Countrydetails/). For functionality resembling our `get_countries` function, another example can be found [here](https://pypi.org/project/geopy/).

However, to the best of our knowledge, there is no existing PyPI package that offers a dedicated function to verify whether a city is located in a specified country. The strength of our package lies in its locally stored data and specialized functions that facilitate searches based on city names, offering a more versatile and comprehensive approach.

## Installation

```bash
$ pip install worldfinder
```

## Documentation

Our online documentation can be found [here](https://worldfinder.readthedocs.io/en/latest/?badge=latest).

## Usage

Once you install worldfinder using pip, you can access the following functions as shown below in the examples.

1. **Getting the Capital City of a Country**:
   The `get_capital` function returns the capital city of the given country.

   ```python
   from worldfinder.get_capital import get_capital

   capital_city = get_capital("countryName") # Replace countryName with the actual country name
   print(capital_city) # This will print out the capital city of a country
   ```

2. **Getting all Countries that Contain a City**:
   The `get_countries` function will return a list of countries where the given city name exists in.

   ```python
   from worldfinder.get_countries import get_countries

   # Get list of countries containing a city
   country_list = get_countries("cityName") # Replace cityName with the actual city name
   print(country_list)  # Prints a list of countries containing the city
   ```

3. **Checking if a City Exists in a Country**:
   The `check_city` function checks if the given city name is a city in the given country.

   ```python
   from worldfinder.check_city import check_city

   city_exists = check_city("cityName", "countryName") # Replace strings with actual values
   print(city_exists)  # Returns True if the city exists in the country otherwise False
   ```

4. **Getting a Country's Statistic**:
   The `get_country_statistic` function returns the country statistic for the specified country. Currently there are 5 acceptable options for country statistics (gdp, population, cpi, birth rate, unemployment rate)

   ```python
   from worldfinder.get_country_statistic import get_country_statistic
   statistic = get_country_statistic("countryName", "statistic") # Replace strings with actual values
   print(statistic)  # Prints the country's statistic
   ```

### Running Tests

To make sure the worldfinder package is working properly on your system, you can run the testing scripts with `pytest. This will require you to have pytest installed on your system.

```bash
$ pip install pytest
```

You will then need to clone the repository on to your machine and navigate to the root directory. Once that is done you can execute the following command to run our testing scripts:

```bash
$ pytest
```

To get a view of the test coverage, you can run the following command:

```bash
$ pytest --cov=src/worldfinder
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`worldfinder` was created by Group 17. It is licensed under the terms of the MIT license.

## Credits

`worldfinder` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors
- Brian Chang
- Michael Gelfand 
- Elaine Chu
- Coco Shi