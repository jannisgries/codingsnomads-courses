'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

##############################################################
# TO-DOS before running script
##############################################################
# Create VENV and install requirements as of requirements.txt

##############################################################
# Script Initialization
##############################################################
import inquirer
import sqlalchemy
import requests
from pprint import pprint

# CLI general Vars
horizontal_line = "__________________________________________"

# SQL - General Vars
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:dewrEg-sumden-degde6@localhost/tasks', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
insp = sqlalchemy.inspect(engine)

# API - General Vars
user_api_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
tasks_api_url = 'http://demo.codingnomads.co:8080/tasks_api/tasks'


##############################################################
# Check if table exists, if not, create such
##############################################################

def create_tables():
    tables_to_create = ["tasks", "users"]       
    insp = sqlalchemy.inspect(engine)
    database_tables = insp.get_table_names()
    created_tables = {}
    for table in tables_to_create:
        if table not in database_tables:
            if table == "users":
                columns = [
                    sqlalchemy.Column('id', sqlalchemy.Integer(), nullable=False, primary_key=True),
                    sqlalchemy.Column('email', sqlalchemy.String(255)),
                    sqlalchemy.Column('first_name', sqlalchemy.String(255)),
                    sqlalchemy.Column('last_name', sqlalchemy.String(255)),
                    sqlalchemy.Column('created_at', sqlalchemy.String(255)), # has to be string, because sql cant handle such big ints
                    sqlalchemy.Column('updated_at', sqlalchemy.String(255))# has to be string, because sql cant handle such big ints
                ]
            elif table == "tasks":
                columns = [
                    sqlalchemy.Column('id', sqlalchemy.Integer(), nullable=False, primary_key=True),
                    sqlalchemy.Column('userId', sqlalchemy.Integer()),
                    sqlalchemy.Column('name', sqlalchemy.String(255)),
                    sqlalchemy.Column('description', sqlalchemy.String(5000)),
                    sqlalchemy.Column('created_at', sqlalchemy.String(255)), # has to be string, because sql cant handle such big ints
                    sqlalchemy.Column('updated_at', sqlalchemy.String(255)), # has to be string, because sql cant handle such big ints
                    sqlalchemy.Column('completed', sqlalchemy.Boolean())
                ]
            created_tables[table] = sqlalchemy.Table(table, metadata, *columns)
    
    metadata.create_all(engine)
    insp = sqlalchemy.inspect(engine)

def get_data_from_api(api):
    response = requests.get(api)
    # add the returned tasks to the local storage variable of the user
    if response.status_code == 200: 
        data = response.json()['data']
        return data
    # Error handling
    else: 
        print("\nSorry, something went wrong - Please try again.")
        print(f"\n{horizontal_line}\n")

def check_if_dbentry_exists(table, key, value):
    query = sqlalchemy.select(table).where(getattr(table.columns, key) == value)
    result = connection.execute(query)
    r = result.fetchall()
    if r == []:
        return False
    else:
        return True

##############################################################
# Programme Logic
##############################################################

##############################################################
#  Create Tables, if necessary
create_tables()

##############################################################
#  Get User Data from API and transist it to local database
#  Get Data 
user_data = get_data_from_api(user_api_url)
table = sqlalchemy.Table('users', metadata, autoload_with=engine)
query = sqlalchemy.insert(table)
new_users = []
for user in user_data:
    user_exists = check_if_dbentry_exists(table, 'id', user['id'])
    if user_exists == False:
        # new_record = {
        #     'id': user.id,
        #     'email': user.email,
        #     'first_name': user.first_name,
        #     'last_name': user.last_name,
        #     'created_at': user.created_at,
        #     'updated_at': user.updated_at
        # }
        new_users.append(user)

result = connection.execute(query, new_users)     


##############################################################
#  Get Tasks Data from API and transist it to local database

#  Tasks Data 
tasks_data = get_data_from_api(tasks_api_url)
table = sqlalchemy.Table('tasks', metadata, autoload_with=engine)
query = sqlalchemy.insert(table)
new_tasks = []
for task in tasks_data:
    task_exists = check_if_dbentry_exists(table, 'id', task['id'])
    if task_exists == False:
        # new_record = {
        #     'id': user.id,
        #     'email': user.email,
        #     'first_name': user.first_name,
        #     'last_name': user.last_name,
        #     'created_at': user.created_at,
        #     'updated_at': user.updated_at
        # }
        new_tasks.append(task)
result = connection.execute(query, new_tasks)    