install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run -u alexey -p 1

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	clear
	poetry run flake8 gendiff tests

test:
	clear
	poetry run pytest -vv

check: lint test

gendiff:
	poetry run gendiff


.PHONY: gendiff