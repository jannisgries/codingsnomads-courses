import sqlalchemy
from pprint import pprint
############################
# Engine Object
engine = sqlalchemy.create_engine('mysql+pymysql://root:dewrEg-sumden-degde6@localhost/sakila', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

class Actor: 
    def __init__(self, actor_id, first_name, last_name, last_update) -> None:
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    def __str__(self) -> str:
        return f"First name: {self.first_name}, Last name: {self.last_name} was updated {self.last_update}"
    

# ############################
# Retrieve Data
# ############################
# Normal Select
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
query = sqlalchemy.select(actor)

# Join Tables 
# film = sqlalchemy.Table('film', metadata, autoload_with=engine)
# actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)
# film_actor = sqlalchemy.Table('film_actor', metadata, autoload_with=engine)
# joint_tables = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
# query = sqlalchemy.select(film.columns.film_id, film.columns.title, actor.columns.first_name, actor.columns.last_name).select_from(joint_tables).where(film.columns.film_id == 999)
############################
result_proxy = connection.execute(query)
# ResultProxy with Keys = Column Names
actor_list = []
for result in result_proxy.mappings():
    new_actor = Actor(result['actor_id'], result['first_name'], result['last_name'], result['last_update'])
    actor_list.append(new_actor)


for actor in actor_list:
    print(actor)

# for el in result:
#     result_list.append(el._mapping)
# pprint(result_list)



# result = result_proxy.fetchone() # fetchone() / fetchall()
# for row in result:
#     print(row)


# for row in result_proxy:
#     row_as_dict = row._mapping


# # Iterate over result_prox
# for result in result_proxy:
#     print(result)









# ############################
# # Create Table
# ############################

# new_table = sqlalchemy.Table('new_table', metadata,
#                              sqlalchemy.Column('id', sqlalchemy.Integer()),
#                              sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False),
#                              sqlalchemy.Column('salary', sqlalchemy.Float(), default=100.0)                             
#                              )

# metadata.create_all(engine)



# ############################
# # Insert Data
# ############################
# new_table = sqlalchemy.Table('new_table', metadata, autoload_with=engine)
# ## Single Line Insert
# query = sqlalchemy.insert(new_table).values(id=1, name='Software Ninjaneer', salary=60000.00)
# proxy = connection.execute(query)
# ## Multiple Line Inserts
# query = sqlalchemy.insert(new_table)
# new_records = [{'id':'2', 'name':'record1', 'salary':80000, 'active':False},
#                {'id':'3', 'name':'record2', 'salary':70000, 'active':True}]
# result_proxy = connection.execute(query,new_records)

# ############################
# # Update Data
# ############################
# new_table = sqlalchemy.Table('new_table', metadata, autoload_with=engine)
# query = sqlalchemy.update(new_table).values(salary=90000.00).where(new_table.columns.id == 1)
# proxy = connection.execute(query)

# ############################
# # Delete Data
# ############################
# new_table = sqlalchemy.Table('new_table', metadata, autoload_with=engine)
# query = sqlalchemy.delete(new_table).where(new_table.columns.id == 1)
# proxy = connection.execute(query)


