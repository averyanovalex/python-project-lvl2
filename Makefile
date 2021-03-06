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

onetest: # run one tests
	clear
	poetry run pytest tests/test_hexlet.py::test_json_plain

check: # run linter and tests
	poetry run flake8 gendiff tests
	poetry run pytest --cov=gendiff tests/ --cov-report xml
	
cov: # show tests coverage report
	poetry run coverage report

gendiff: # run gendiff without arguments
	poetry run gendiff

gendiff_json: # run gendiff for 2 json files
	poetry run gendiff 	'tests/fixtures/file1.json' 'tests/fixtures/file2.json' --format stylish

gendiff_json_complex: # run gendiff for 2 json files (complex structure)
	poetry run gendiff 	'tests/fixtures/file_complex1.json' 'tests/fixtures/file_complex2.json'

gendiff_yaml: # run gendiff for 2 yaml files
	poetry run gendiff 	'tests/fixtures/file1.yaml' 'tests/fixtures/file2.yaml'

gendiff_yaml_complex: # run gendiff for 2 yaml files
	poetry run gendiff 	'tests/fixtures/file_complex1.yaml' 'tests/fixtures/file_complex2.yaml'

gendiff_json_plain: # run gendiff for 2 json files (complex structure, format: plain)
	poetry run gendiff 	--format plain 'tests/fixtures/file_complex1.json' 'tests/fixtures/file_complex2.json'

gendiff_json_json: # run gendiff for 2 json files (complex structure, format: json)
	poetry run gendiff 	--format json 'tests/fixtures/file_complex1.json' 'tests/fixtures/file_complex2.json'

hexlet: # run hexlet files
	poetry run gendiff 	--format plain 'tests/fixtures/hexlet/file1.json' 'tests/fixtures/hexlet/file2.json'

.PHONY: gendiff
