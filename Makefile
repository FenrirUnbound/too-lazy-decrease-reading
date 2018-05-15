.PHONY: clean docker-build docker-build-ui docker-install docker-test docker-venv run

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

docker-build:
	docker build -t toolazy .

docker-build-ui:
	docker run --rm -ti -v `pwd`/ui:/usr/src/ui node:8 /bin/sh -c \
		"cd /usr/src/ui \
		&& npm run build"
	mkdir -p ./app/static
	cp -R ./ui/build/* ./app/static
	mv ./app/static/static/js ./app/static/js
	mv ./app/static/static/css ./app/static/css
	mv ./app/static/static/media ./app/static/media
	rm -rf ./app/static/static

docker-install:
	docker run --rm -v `pwd`/app:/usr/src/app python:3 /bin/sh -c \
		"cd /usr/src/app \
		&& . venv/bin/activate; pip install -Ur requirements.txt"

docker-install-ui:
	docker run --rm -v `pwd`/ui:/usr/src/ui node:8 /bin/sh -c \
		"cd /usr/src/ui \
		&& npm install"

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

run:
	docker run --rm -ti -p 8080:8080 toolazy:latest
