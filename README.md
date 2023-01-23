# SkyPro Python Course #


## Mashtaler Maksim 01/2023
API for electronics retail network

# Description #


### Stack ###
- python3.9, Django - backend
- Postgres - database


## Features ##

1. Authentication (electronics_store/core)
   - django authentication
   - profile update
2. Main logic (electronics_store/e_chain)
   - full CRUD with filters
     * Information about all network objects;
     * Information about the objects of a certain country (filter by name);
     * Statistics on objects whose debt exceeds the average debt of all objects;
     * All network objects where a certain product can be found (filter by product id);
     * Ability to create and delete a network object and a product;
     * Ability to update the data of the network object and the product (prohibit updating the "Debt to supplier" field via the API);
   - permissions are correctly configured to read/update/delete for all entities
   - admin panel with filter by city name, "administrator action" that clears the debt to the supplier from the selected objects.
3. Tests for whole CRUD user apps (./tests)


## How to: ##

## Development local configuration ##
1) Create venv
2) Install dependencies
   - `pip install -r requirements.txt`
3) Run docker container for postgres
   - `docker-compose -f deploy/docker-compose.db.yaml up -d`
4) Make migrations
   - `cd electronics_store`
   - `manage.py makemigrations`
   - `manage.py migrate`
5) Run server 
   - `manage.py runserver`
6) Createsuperuser
   - `manage.py createsuperuser`
7) Connect to admin panel at http://127.0.0.1:8000/admin/
8) Run tests from main folder
   - `pytest`


## Project links
1) Admin - http://127.0.0.1:8000/admin/
2) Swagger - http://127.0.0.1:8000/api/schema/swagger-ui/