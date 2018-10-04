<<<<<<< HEAD
Learnings accomplished:
Run Mongo db in a Docker container.
main.py is a python script that connects to a mongo db.
main.py pulls information from the test.db.
information can be viewed on endpoints. 
e.g. localhost:5000
      localhost:5000/stores
      localhost:5000/users
      localhost:5000/stores/id/<id #>
=======
# Flask-Mongo

A REST API powered by Flask and MongoDB.

# Requirements

* Docker
* Python 3
* Virtualenv (or your preferred Python environment)

## Suggested Tools

* Robo3T

# Setup

Create a virtual environment for this project.

```
virtualenv -p $(which python3) ~/venv/flask-mongo
```

Activate your virtual environment.

```
source ~/venv/flask-mongo
```

Install project requirements.

```
pip install -r requirements.txt
```

# Run

## App

Run the app at `localhost:5000`.

```
python -m api.main
```

## Docker

Start MongoDB in a docker container.

```
docker-compose up
```

Stop MongoDB container but do not clear data (start with same data on container restarts).

```
docker-compose down
```

Stop MongoDB container and clear data (start with fresh data on container restart).

```
docker-compose down -v
```
>>>>>>> flask-mongo/master
