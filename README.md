# Ticket price service

FastAPI service providing ticket price prediction

## Getting started

```sh
pip install poetry
poetry install
poetry run pre-commit install
```

## Useful commands

```sh
# start in dev mode
poetry run uvicorn src.ticket_price_api.main:app --reload

# run docker locally
poetry export -o requirements.txt && docker run -p 8000:8000 --rm -it $(docker build -q .)

# lint & format all files (e.g. after rebase / commit --no-verify)
poetry run ruff check --fix
poetry run ruff format
```
