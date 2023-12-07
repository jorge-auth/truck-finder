## Instalation procedure

Install the dependencies from the file "requirements.txt"

    pip install -r requirements.txt


Run the migrations,

    python3 manage.py migrate


Load the database with the fixtures

    python3 manage.py loaddata clusters_fixture.json foodtruck_fixture.json

Run the development server

    python3 manage.py runserver 0:8000


## Run tests

At the command line project root, run
    
    pytest

## Interact with the rest api

An http client of your choice and access the url. For example

    http://localhost:8000/api/v1/foodtrucks/?lat=37.7749&lon=-162.4194