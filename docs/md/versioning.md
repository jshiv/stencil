Versioning
====================================================================================================

### Prerequisites
* git tag
	git tag -a v0.1.0 -m "0.1.0"
* versioneer install
	pip install git+https://github.com/warner/python-versioneer.git


### running versioneer

follow the instructions for versioneer: https://github.com/warner/python-versioneer

navigate to the root directory folder and run:

	versioneer install


### tagging git version

	git tag -a v1.0.0 -m "version 1.0.0"
	git push --tags

### deploying to PiPy

https://python-packaging-user-guide.readthedocs.org/en/latest/distributing.html

	sudo python setup.py install
	sudo python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*