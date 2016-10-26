all:
	true

release:
	make tox
	make push
	make bump
	make push
	make pypi
	make clean

tox:
	tox

bump:
	bumpversion patch

push:
	git push
	git push --tags

pypi:
	python setup.py register
	python setup.py sdist upload

clean:
	rm -rf build dist pkg src *.egg-info valkit-*.tar.gz
	find -name __pycache__ | xargs rm -rf

clean-all: clean
	rm -rf .tox .coverage .cache
