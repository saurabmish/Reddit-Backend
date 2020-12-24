[![saurabmish](https://circleci.com/gh/saurabmish/Reddit-Backend.svg?style=shield)](https://circleci.com/gh/saurabmish/Reddit-Backend)
[![codecov](https://codecov.io/gh/saurabmish/Reddit-Backend/branch/master/graph/badge.svg?token=M7L0AOGKGY)](https://codecov.io/gh/saurabmish/Reddit-Backend)

# Reddit Backend

Revisiting [CPSC 449 group project][1] taken in Spring 2020

Flask microservices for create, read, update, and delete (CRUD) operations.

Implemented with test-driven development approach.

**What's new this time?**

  + CI / CD pipelines using [CircleCI][2]
  + Source code and test coverage integration
  + Postgres database instead of sqlite
  + Better application design
  + Project milestones using git tags
  + Segregated unit, functional, and load testing

## Setup

  + Navigate to the project's root directory

  + Create a Python 3 virtual environment:

    `python3 -m venv reddit-backend`

  + Activate newly created virtual environment:

    `source reddit-backend/bin/activate`

  + Update *pip* package manager:

    `pip install --upgrade pip`

  + Install required packages in the virtual environment:

    `pip install --requirement requirements.txt`

  + Set `PYTHONPATH`:

    `export PYTHONPATH=$PWD`

### Unit Testing

  + Run test cases:

    `pytest -v`

  + Check source code **and** test coverage:

    `pytest -v --cov`

### API Testing

  + Execute application:

    `flask run`

  + Navigate to API testing directory:

    `cd tests/api`

  + Ensure that all scripts are executable:

    `chmod +x *.sh`

  + Create users:

    `./create_user_accounts.sh`

  + Get all users:

    `./get_all_users.sh`

[1]: https://github.com/sean-maclane/cpsc-449-group-c-project
[2]: https://circleci.com/
