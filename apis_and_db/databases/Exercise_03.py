'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''
import sqlalchemy
############################
# Engine Object
engine = sqlalchemy.create_engine('mysql+pymysql://root:dewrEg-sumden-degde6@localhost/sakila', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
############################
# Tables 
film = sqlalchemy.Table('film', metadata, autoload_with=engine)
# ############################
# Update-Query

query = sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length > 150)
result = connection.execute(query)
