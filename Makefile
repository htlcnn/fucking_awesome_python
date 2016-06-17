all:
	flake8 *.py

req:
	pip install -r requirements.txt

init: req
