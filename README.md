# VR1 Family Backend

VR1 Family Charity Aid Services is an Australian organisation that aims to provide immediate humanitarian assistance

## Issues
1. If no environment variables have been defined, do the following (example):
```
export FLASK_APP=application.py
export FLASK_ENV=development
```
2. There might be inconsistencies across the databases, so we can add `db.drop_all()` in `application.py` to remove all the databases