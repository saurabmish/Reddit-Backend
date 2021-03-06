[![Maintainability](https://api.codeclimate.com/v1/badges/1ce53ea9c1a7c71726c7/maintainability)](https://codeclimate.com/github/saurabmish/Reddit-Backend/maintainability)
[![saurabmish](https://circleci.com/gh/saurabmish/Reddit-Backend.svg?style=shield)](https://circleci.com/gh/saurabmish/Reddit-Backend)
[![codecov](https://codecov.io/gh/saurabmish/Reddit-Backend/branch/master/graph/badge.svg?token=M7L0AOGKGY)](https://codecov.io/gh/saurabmish/Reddit-Backend)

# Reddit Backend

Revisiting [CPSC 449 group project][1] taken in Spring 2020

**About**

This project is about building microservices for a web application. Each microservice emulates a core functionality of Reddit. Since this project has no front-end, there are comprehensive automation test suites to check every functionality of the application.

**What's new this time?**

  + CI / CD pipelines using [CircleCI][2]
  + Application containerized with [Docker][3]
  + Source code and test [coverage][4] integration
  + [Postgres][5] database instead of sqlite
  + Significantly increased [maintainability][6]
  + Segregated unit, integration, functional, and load testing
  + Better application design and comprehensive documentation
  + Project [milestones][7] using git tags

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

### Integration Testing

  + Run test cases:

    `pytest -v`

  + Check source code **and** test coverage:

    `pytest -v --cov`

### API Testing

  + Execute application:

    `flask run`

  + Open a new terminal and navigate to API testing directory:

    `cd tests/unit/accounts`

  + Ensure that all scripts are executable:

    `chmod +x *.sh`

  + Create users:

    `./create.sh`

  + Update email:

    `./update_email.sh`

  + Modify karma:

    `./modify_karma.sh`

  + Delete user:

    `./delete.sh`


[1]: https://github.com/sean-maclane/cpsc-449-group-c-project
[2]: https://circleci.com/product/
[3]: https://www.docker.com/why-docker
[4]: https://coverage.readthedocs.io/en/coverage-5.3.1/
[5]: https://www.postgresql.org/
[6]: https://codeclimate.com/github/saurabmish/Reddit-Backend
[7]: https://github.com/saurabmish/Reddit-Backend/releases
