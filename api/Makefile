.PHONY: format typecheck test

PROJECT_DIR=giveaway
TESTS_DIR=tests

all: format

format:
	black ${PROJECT_DIR}

typecheck:
	mypy ${PROJECT_DIR}

test:
	pytest ${TESTS_DIR}
