# Book-Retrieval API
The repository contains a RESTful API built with Flask for retrieving books from the database. You can use the following endpoints:


`[GET] /bookapi/books/:id` - Fetching a single book by its id.
`[GET] /bookapi/books` - Fetching all books

**Note**: <i> The data is hardcorded to keep the tutorial simple, nothing fancy :)</i>
## Running the API

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

## Running only grouped Tests
To only execute the `get_request` grouped tests, run the following command:

```bash
pytest -m get_request
```
