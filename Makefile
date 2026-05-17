deps:
	pip install -r requirements.txt

lint:
	flake8 main.py test_main.py

test:
	pytest test_main.py

run:
	python main.py
