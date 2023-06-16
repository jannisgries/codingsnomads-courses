'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint
############################
# Engine Object
engine = sqlalchemy.create_engine('mysql+pymysql://root:dewrEg-sumden-degde6@localhost/sakila', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

############################
# Join Tables 
film = sqlalchemy.Table('film', metadata, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload_with=engine)
joint_tables = film.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)

# ############################
# Retrieve Data
query = sqlalchemy.select(film.columns.title, category.columns.name).select_from(joint_tables)
result_proxy = connection.execute(query)

# ############################
# Print Result
for result in result_proxy:
    pprint(result)