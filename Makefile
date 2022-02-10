install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run -u alexey -p 1

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gen_diff

gendiff:
	poetry run gendiff
