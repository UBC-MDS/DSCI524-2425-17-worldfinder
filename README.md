# worldfinder

This packages provides a set of four functions for working with geographical information about cities and countries. These functions will allow users to find the capital city of a country, find all countries that contain a given city name, determine if a city belongs to a specific country, and get statistics about a specified country such as population, GDP, and surface area. These functions will utilize a pre-existing database of city and country information to return the necessary information.

## Installation

```bash
$ pip install worldfinder
```

## Usage

- TODO

## Functions and Data
### Data
- The data for this library will consist of an object containing all countries and their respective capitals
### Functions
- getCapital(country) 

        This function will retrieve the capital given a country name passed as an input from a local data object consisting of capital and country data.

- getCountries(city)

        This function searches for a specified city and returns a list of unique countries where the city is located.

- checkCity(city, country)

        This function will return a boolean on if the given city exist in the given country.

- getCountryStatistic(country, statistic)

        This function will return a integer or float representing a specified statistic for a given country.

## worldfinder in the Python Ecosystem
The PyPI server hosts numerous packages related to country and city data. Among these, we have identified a few noteworthy examples that offer functionality similar to our package. For instance, a package with functionality similar to our getCapital function can be found [here](https://pypi.org/project/country-capitals/). Similarly, a package providing features comparable to our countryinfo function, which retrieves information about a specified country, is available [here](https://pypi.org/project/Countrydetails/). For functionality resembling our getCountries function, another example can be found [here](https://pypi.org/project/geopy/).

However, to the best of our knowledge, there is no existing PyPI package that offers a dedicated function to verify whether a city is located in a specified country. The strength of our package lies in its locally stored data and specialized functions that facilitate searches based on city names, offering a more versatile and comprehensive approach.

## Contributors
- Brian Chang
- Michael Gelfand
- Elaine Chu
- Coco Shi

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`worldfinder` was created by Group 17. It is licensed under the terms of the MIT license.

## Credits

`worldfinder` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
