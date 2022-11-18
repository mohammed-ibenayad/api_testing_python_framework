# Building a COMPLETE API Test Automation Framework with Python & Pytest

## Purpose

This is a complete example of a Test Automation Framework build with Python and Pytest library. In this example, some clean code design 
principles have been applied to reduce code decoupling. 

## Setup

Ensure you have
[pipenv already installed](https://pypi.org/project/pipenv/#installation):

```zsh
# Activate virtualenv.
pipenv shell
# Install all dependencies in your virtualenv.
pipenv install
```

## Main libraries used and Why

`assert_py`: 
`jsonpath_ng`:
`cerberus`: 

## How to navigate & Code Design

```zsh
/assertions
```


## Application under test

This automated test suite covers features of `petstore-api`, Please refer the Swagger Petstore OpenAPI specs
[here](https://petstore.swagger.io/).

## How to run

```zsh

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto

```

## Discuss?

Feel free to use the
[Github discussions](https://github.com/mohammed-ibenayad/api_testing_python_framework/discussions/1)
in this repo to ✍🏼 your thoughts.

Happy Automation Testing!
