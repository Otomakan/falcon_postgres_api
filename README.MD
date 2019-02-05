Thanks to https://github.com/wileykestner/falcon-sqlalchemy-demo/
To start the project don't forget to create .env file and add
DB_URL=${NAME OF YOUR DATABASE}

Make sure you have pip intalled as well as a running postgres database.

To create migration scripts simply run 
```
alembic revision -m "create account table"
```
Then update the upgrade() and downgrade() functions accordingly in the generated file.

A very useful feature of alembic is Auto Generating Migrations.
```
alembic revision --autogenerate -m "create some table"
```
This will detect all the changes made in the models imported in the  models/__init__.py file
Make sure you import your new Models in that file.



Use the alembic documentation to perform your migrations: https://alembic.sqlalchemy.org/en/latest/

