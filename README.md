# VR1 Family Backend

VR1 Family Charity Aid Services is an Australian organisation that aims to provide immediate humanitarian assistance


## How To Run
1. Be sure to install the following (e.g pip3 install flask): 
    * Flask
    * SQLAlchemy
    * python-dotenv
    * (any other necessary dependencies)
2. Run the app by heading over to `application.py` and type `flask run`


## Issues
1. If no environment variables have been defined, do the following (example):
```
export FLASK_APP=application.py
export FLASK_ENV=development
```
2. There might be inconsistencies across the databases, so add `db.drop_all()` in `application.py` to remove all the databases