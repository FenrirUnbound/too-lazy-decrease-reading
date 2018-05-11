.PHONY: clean docker-build docker-install docker-test docker-venv run

docker-build:
	docker build -t toolazy .

docker-install:
	docker run --rm -v `pwd`/app:/usr/src/app python:3 /bin/sh -c \
		"cd /usr/src/app \
		&& . venv/bin/activate; pip install -Ur requirements.txt"

docker-old-test:
	docker run --rm \
		-v `pwd`/app:/usr/src/app \
		-v `pwd`/test:/usr/src/test \
		python:3 /bin/sh -c \
			"cd /usr/src/app \
			&& . venv/bin/activate \
			&& cd /usr/src \
			&& cp test/test_status.py . \
			&& touch /usr/src/__init__.py \
			&& pytest"

docker-test:
	docker run --rm \
		-v `pwd`/app:/usr/src/app \
		python:3 /bin/sh -c \
			"cd /usr/src/app \
			&& . venv/bin/activate \
			&& python -c \"import nltk; nltk.download('punkt')\"\
			&& nosetests -v ./test"

docker-venv:
	docker run --rm -v `pwd`/app:/usr/src/app python:3 /bin/sh -c \
		"pip install virtualenv \
		 && /usr/local/bin/virtualenv /usr/src/app/venv \
		 && . /usr/src/app/venv/bin/activate \
		 && touch /usr/src/app/venv/bin/activate \
		 && chmod +x /usr/src/app/venv/bin/activate"

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

run:
	docker run --rm -ti -p 8080:8080 toolazy:latest