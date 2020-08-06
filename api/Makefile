.PHONY: format typecheck test lint

PROJECT_DIR=giveaway
TESTS_DIR=tests

all: test typecheck lint format

format:
	black ${PROJECT_DIR}

typecheck:
	mypy ${PROJECT_DIR}

test:
	pytest ${TESTS_DIR}

lint:
	flake8 ${PROJECT_DIR}
