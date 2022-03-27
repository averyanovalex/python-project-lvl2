install: # install all required dependencies  (before install poetry)
	poetry install

build: # build package
	poetry build

publish: # publish package in pypi.org test 
	poetry publish --dry-run -u alexey -p 1

package-install: # install package locally
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: # linter check code
	clear
	poetry run flake8 gendiff tests

test: # run tests
	clear
	poetry run pytest -vv

check: # run linter and tests
	poetry run flake8 gendiff tests
	poetry run pytest --cov=gendiff tests/ --cov-report xml
	
cov: # show tests coverage report
	poetry run coverage report

gendiff: # run gendiff without arguments
	poetry run gendiff

gendiff_json: # run gendiff for 2 json files
	poetry run gendiff 	'tests/fixtures/file1.json' 'tests/fixtures/file2.json'

gendiff_yaml: # run gendiff for 2 yaml files
	poetry run gendiff 	'tests/fixtures/file1.yaml' 'tests/fixtures/file2.yaml'  --format yaml


.PHONY: gendiff
