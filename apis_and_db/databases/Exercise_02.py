'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''
import sqlalchemy
from pprint import pprint
############################
# Engine Object
engine = sqlalchemy.create_engine('mysql+pymysql://root:dewrEg-sumden-degde6@localhost/sakila', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

############################
# Tables and Joint ones 
film = sqlalchemy.Table('film', metadata, autoload_with=engine)
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
category = sqlalchemy.Table('category', metadata, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', metadata, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', metadata, autoload_with=engine)
joint_film_category = film.join(film_category, film_category.columns.film_id == film.columns.film_id).join(category, category.columns.category_id == film_category.columns.category_id)
joint_actor_film = actor.join(film_actor, film_actor.columns.actor_id == actor.c.actor_id).join(film, film.c.film_id == film_actor.columns.film_id)
joint_film_actor_category = joint_film_category.join(film_actor, film_actor.c.film_id == film.c.film_id).join(actor, actor.c.actor_id == film_actor.c.actor_id)
# ############################
# # Select all the actors with the first name of your choice
# query = sqlalchemy.select(actor).where(actor.columns.first_name == "John")
# result = connection.execute(query)
# for row in result:
#     print(row)

# ############################
# # Select all the actors and the films they have been in
# query = sqlalchemy.select(actor.c.first_name, actor.c.last_name, film.c.title).select_from(joint_actor_film)
# result = connection.execute(query)
# for row in result:
#     print(row)

# ############################
# # Select all the actors that have appeared in a category of a comedy of your choice
# query = sqlalchemy.select(actor.c.first_name, actor.c.last_name).select_from(joint_film_actor_category).where(film_category.c.category_id == 5).distinct().order_by(sqlalchemy.asc(actor.c.last_name))
# result = connection.execute(query)
# for row in result:
#     print(row)


# # ############################
# # # Select all the comedic films and sort them by rental rate
# query = sqlalchemy.select(film.c.title, film.c.rental_rate).select_from(joint_film_category).where(film_category.c.category_id == 5).distinct().order_by(sqlalchemy.desc(film.c.rental_rate))
# result = connection.execute(query)
# for row in result:
#     print(row)

# # ############################
# # Using one of the statements above, add a GROUP BY statement of your choice
# query = sqlalchemy.select(actor.c.first_name, actor.c.last_name, sqlalchemy.func.count(film.c.title)).select_from(joint_film_actor_category).group_by(actor.c.actor_id).order_by(sqlalchemy.asc(actor.c.actor_id))
# result = connection.execute(query)
# for row in result:
#     print(row)

# # ############################
# # Using one of the statements above, add a ORDER BY statement of your choice
# query = sqlalchemy.select(film.c.title, film.c.rental_rate).select_from(joint_film_category).where(film_category.c.category_id == 5).distinct().order_by(sqlalchemy.desc(film.c.rental_rate))
# result = connection.execute(query)
# for row in result:
#     print(row)
