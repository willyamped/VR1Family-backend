# VR1 Family Backend

VR1 Family Charity Aid Services is an Australian organisation that aims to provide immediate humanitarian assistance

## How To Create a Virtual Environment
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `deactivate` to deactivate

## How To Run
1. Be sure to install the following (e.g `pip3 install flask`): 
    * Flask
    * flask_sqlalchemy
    * python-dotenv
    * flask-cors
    * (any other necessary dependencies)
2. Run the app by heading over to `application.py` and type `flask run`

## How To See Data in Database
1. Perform the following command `sqlite3 instance/data.db`
2. Perform the query (e.g `SELECT * FROM item`)

## How to 

## Issues
1. If no environment variables have been defined, do the following (example):
```
export FLASK_APP=application.py
export FLASK_ENV=development
```
2. There might be inconsistencies across the databases, so add `db.drop_all()` in `application.py` to remove all the databases
3. If there's a CORS policy error in the client-side, be sure to add a "/" at the end of the end-point