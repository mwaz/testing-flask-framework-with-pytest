# TESTING FLASK FRAMEWORK WITH PYTEST

[![CircleCI](https://circleci.com/gh/mwaz/testing-flask-framework-with-pytest.svg?style=svg)](https://circleci.com/gh/mwaz/testing-flask-framework-with-pytest)

<p align="center"><img src="https://avatars3.githubusercontent.com/u/59034516"></p>


The repository contains a RESTful API built with Flask for retrieving books from a list object defined in the API. You can use the following endpoints:

`[GET] /bookapi/books/:id` - Fetching a single book by its id.
`[GET] /bookapi/books` - Fetching all books

**Note**: <i> The data is hardcorded to keep the tutorial simple, nothing fancy :)</i>
## Installation
---
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running the Application

FLASK_APP=api.py flask run

## Execution all the Tests
To execute all the tests, run the following command:

```bash
pytest 
```

## Execution all the Tests with stdout response
To execute all the tests, run the following command:

```bash
pytest -s
```

## Executing only grouped Tests
To only execute the `get_request` grouped tests, run the following command:

```bash
pytest -m get_request
```

## Details

This repo is built following a tutorial published on CircleCI blog under the CircleCI Guest Writer Program.

- Blog post: [Testing Flask Framework with Pytest][blog]
- Author's GitHub profile: [Waweru Mwaura][author]

### About CircleCI Guest Writer Program

Join a team of freelance writers and write about your favorite technology topics for the CircleCI blog. Read more about the program [here][gwp-program].

Reviewers: [Ron Powell][ron], [Stanley Ndagi][stan]


[blog]: https://circleci.com/blog/testing-flask-framework-with-pytest/
[author]: https://github.com/mwaz

[gwp-program]: https://circle.ci/3ahQxfu
[ron]: https://github.com/ronpowelljr
[stan]: https://github.com/NdagiStanley