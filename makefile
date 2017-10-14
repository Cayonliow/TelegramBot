.PHONY: test

n:
	./ngrok http 5000

run:
	python3 app.py

all:
	./ngrok http 5000
	python3 app.py
