# File Counter now writes to MySQL-Database
import pathlib
import csv
import sqlalchemy
import datetime
from pprint import pprint
import json
import inquirer

# General Vars
horizontal_line = "__________________________________________"

# SQL - General Vars
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:dewrEg-sumden-degde6@localhost/filecount', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
insp = sqlalchemy.inspect(engine)

#########################################################
# General functions
#########################################################

def ask_user_options(inq_name: str, question: str, choices: list) -> str:
    """Ask user, which action he would like to take
    Returns:
        str: Chosen option
    """
    questions = [
        inquirer.List(
            inq_name,
            message=question,
            choices=choices,
        ),
    ]
    chosen_task = inquirer.prompt(questions)[inq_name]
    print(chosen_task)
    print(f"\n{horizontal_line}\n")
    return chosen_task

def create_table(tables_to_create: list):
    """Check if database exists or needs to be created

    Args:
        tables_to_create (list): list containing the names of the tables to create
    """
    tables = {}
    insp = sqlalchemy.inspect(engine)
    database_tables = insp.get_table_names()
    created_tables = {}
    for table in tables_to_create:
        if table not in database_tables:
            columns = []
            if table == "filecount":
                columns = [
                    sqlalchemy.Column('count_id', sqlalchemy.Integer(), nullable=False, primary_key=True),
                    sqlalchemy.Column('time_counted', sqlalchemy.String(255)),
                ]
            elif table == "fileextensions":
                columns = [
                    sqlalchemy.Column('extension_id', sqlalchemy.Integer(), nullable=False, primary_key=True),
                    sqlalchemy.Column('extension_name', sqlalchemy.String(255))
                ]
            elif table == "filecount_fileextensions":
                columns = [
                    sqlalchemy.Column('count_id', sqlalchemy.Integer(), sqlalchemy.ForeignKey("filecount.count_id"),),
                    sqlalchemy.Column('extension_id', sqlalchemy.Integer(), sqlalchemy.ForeignKey("fileextensions.extension_id")),
                    sqlalchemy.Column('count', sqlalchemy.Integer()),

                ]
            elif table == "analyzation":
                columns = [
                    sqlalchemy.Column('analyzation_id', sqlalchemy.Integer(), nullable=False, primary_key=True),
                    sqlalchemy.Column('total_number', sqlalchemy.Integer()),
                    sqlalchemy.Column('content_types', sqlalchemy.String(255)),
                    sqlalchemy.Column('most_files_day', sqlalchemy.String(255)),
                    sqlalchemy.Column('most_common_filetyp', sqlalchemy.String(255))
                ]
               
            created_tables[table] = sqlalchemy.Table(table, metadata, *columns)
            metadata.create_all(engine)
    insp = sqlalchemy.inspect(engine)

def get_column_names(table_name:str) -> list:
    """Get names of columns of a table


    Args:
        table_name (str): name of table

    Returns:
        list: name of columns of this table
    """
    table = sqlalchemy.Table(table_name, metadata, autoload_with=engine)
    query = sqlalchemy.select(table)
    result = connection.execute(query)
    column_names = []
    for r in result.keys():
        column_names.append(r)
    return column_names

#########################################################
# Count file on Desktop
#########################################################
def count_files() -> dict:
    """Counting functionality 

    Returns:
        dict: filetypes and their count as dict
    """
    path_to_desktop = pathlib.Path.home() / "Desktop"
    files_on_desktop = {}
    # Loop through all files on desktop
    for file in path_to_desktop.iterdir():
        # Identify all screenshots on your Desktop
        if file.is_file() == True and file.suffix:
            if file.suffix not in files_on_desktop.keys():
                files_on_desktop.update({file.suffix: 1})
            elif file.suffix in files_on_desktop.keys():
                files_on_desktop[file.suffix] += 1
    return files_on_desktop

def write_count_to_table():
    """Write the count to the database
    """
    # Get the table objects
    table_fileextensions = sqlalchemy.Table('fileextensions', metadata, autoload_with=engine)
    table_filecount = sqlalchemy.Table('filecount', metadata, autoload_with=engine)
    table_filecount_fileextensions = sqlalchemy.Table('filecount_fileextensions', metadata, autoload_with=engine)
    extension_id = {}
    # Check if all file extensions exist and possibly add them to table "fileextensions"
    for file_extension in files.keys():
        query = sqlalchemy.select(table_fileextensions).where(table_fileextensions.columns.extension_name == file_extension)
        result = connection.execute(query)
        r = result.fetchall()
        if  r == []:
            # Entry does not exist,
            que = sqlalchemy.insert(table_fileextensions).values(extension_name = file_extension)
            res = connection.execute(que)
            extension_id[file_extension] = res.inserted_primary_key[0]
        else:
            extension_id[file_extension] = r[0][0]               
    connection.commit()
    # Add Count entry to filecount table 
    dttime = datetime.datetime.now().isoformat(timespec='minutes')
    query = sqlalchemy.insert(table_filecount).values(time_counted = dttime)
    result = connection.execute(query)
    inserted_count_pk = result.inserted_primary_key[0]

    # Add each count to filecount_fileextensions table
    for file_extension, count in files.items():
        query = sqlalchemy.insert(table_filecount_fileextensions).values(count_id = inserted_count_pk, extension_id = extension_id[file_extension], count = count)
        result = connection.execute(query)
    connection.commit()

#########################################################
# Analyse database
#########################################################
def write_analysis_to_table(data_to_insert:dict):
    """Write the analyzation to a new table of db

    Args:
        data_to_insert (dict): values, which should be written to the table
    """
    table_analyzation = sqlalchemy.Table('analyzation', metadata, autoload_with=engine)
    query = sqlalchemy.insert(table_analyzation).values(data_to_insert)
    result = connection.execute(query)
    connection.commit()

def analyse_total_number(returntype: str):
    """Analyse total number vor counted files

    Args:
        returntype (str): type of returnelement (message or value only)
    """
    query = sqlalchemy.select(sqlalchemy.func.sum(table_filecount_fileextensions.columns.count))
    result = connection.execute(query)
    r = result.fetchone()
    if returntype == "message":
        message = f"You have counted {r[0]} files in total\n{horizontal_line}\n"
        return message
    elif returntype == "value":
        value = r[0]
        return value

def analyse_content_types(returntype: str):
    """Analyse content_types and their count

    Args:
        returntype (str): type of returnelement (message or value only)
    """
    jointtable_fileextension = table_fileextensions.join(table_filecount_fileextensions, table_filecount_fileextensions.columns.extension_id == table_fileextensions.columns.extension_id)
    query = sqlalchemy.select(table_fileextensions.columns.extension_name, sqlalchemy.func.sum(table_filecount_fileextensions.columns.count)).select_from(jointtable_fileextension).group_by(table_fileextensions.columns.extension_name)
    result = connection.execute(query)
    r = result.fetchall()
    if returntype == "message":
        message = f"In total, you have counted …\n"
        for el in r:
            message += f"– {el[1]} files w/ content-type {el[0]}\n"
        message += f"{horizontal_line}"
        return message
    elif returntype == "value":
        value = {el[0]: el[1] for el in r}
        return value

def analyse_day_most_files(returntype: str):
    """Analyze the day, youve had the most files

    Args:
        returntype (str): type of returnelement (message or value only)
    """
    jointtable_filecount = table_filecount.join(table_filecount_fileextensions, table_filecount_fileextensions.columns.count_id == table_filecount.columns.count_id)
    query = sqlalchemy.select(table_filecount.columns.time_counted, sqlalchemy.func.sum(table_filecount_fileextensions.columns.count)).select_from(jointtable_filecount).group_by(table_filecount.columns.count_id).order_by(sqlalchemy.desc(sqlalchemy.func.sum(table_filecount_fileextensions.columns.count)))
    result = connection.execute(query)
    r = result.fetchone()
    if returntype == "message":
        message = f"On {r[0].split('T')[0]} at {r[0].split('T')[1]} you have had the most files on your desktop ({r[1]})\n{horizontal_line}"
        return message
    elif returntype == "value":
        value = f"{r[0].split('T')[0]} at {r[0].split('T')[1]} ({r[1]})"
        return value

def analyse_most_common_filetype(returntype: str):
    """Analyze most common filetype

    Args:
        returntype (str): type of returnelement (message or value only)
    """
    jointtable_fileextension = table_fileextensions.join(table_filecount_fileextensions, table_filecount_fileextensions.columns.extension_id == table_fileextensions.columns.extension_id)
    query = sqlalchemy.select(table_fileextensions.columns.extension_name, sqlalchemy.func.sum(table_filecount_fileextensions.columns.count)).select_from(jointtable_fileextension).group_by(table_fileextensions.columns.extension_name).order_by(sqlalchemy.desc(sqlalchemy.func.sum(table_filecount_fileextensions.columns.count)))
    result = connection.execute(query)
    r = result.fetchone()
    if returntype == "message":
        message = f"Your most common file type is {r[0]}, being the type of {r[1]} files in total\n{horizontal_line}"
        return message
    elif returntype == "value":
        value = f"{r[0]} ({r[1]}files)"
        return value

########################################################
# Programme logic / functions execution
#########################################################
# Ask user, what he wants to do
inq_name = "choose_option"
question = "What would you like to do?"
choices = ["Count files on desktop", "Analyse Data", "Quit"]
user_input = ask_user_options(inq_name, question, choices)
while user_input != "Quit":
    if user_input == "Count files on desktop":
        create_table(["filecount", "fileextensions", "filecount_fileextensions"])
        files = count_files()
        write_count_to_table()
        print("Files have been counted successfully")
        print(horizontal_line, end="\n\n")
    elif user_input == "Analyse Data":
        table_fileextensions = sqlalchemy.Table('fileextensions', metadata, autoload_with=engine)
        table_filecount = sqlalchemy.Table('filecount', metadata, autoload_with=engine)
        table_filecount_fileextensions = sqlalchemy.Table('filecount_fileextensions', metadata, autoload_with=engine)
        #############
        inq_name = "choose_option"
        question = "What would you like to do?"
        choices = ["Analyse everything (and write to table)",
                    "Get total number of counted files",
                   "Get total number of specific file type",
                   "Get day with most files on desktop",
                   "Get most common file type",
                   "Quit"]
        chosen_analyzation = ask_user_options(inq_name, question, choices)
        while chosen_analyzation != "Quit":
            # Total number of counted files
            if chosen_analyzation == "Analyse everything (and write to table)":
                create_table(["analyzation"])
                total_number = analyse_total_number("value")
                content_types = analyse_content_types("value")
                most_files_day = analyse_day_most_files("value")
                most_common_filetyp = analyse_most_common_filetype("value")
                data_to_insert = {
                    "total_number": total_number,
                    "content_types": str(content_types),
                    "most_files_day": most_files_day,
                    "most_common_filetyp": most_common_filetyp
                    }
                write_analysis_to_table(data_to_insert)
                print("We can provide you with this analysis: \n")
                for text in data_to_insert.values():
                    print(text)
                    print(f"{horizontal_line}")
                print(f"It has been saved to your analysis table.\n{horizontal_line}")
            elif chosen_analyzation == "Get total number of counted files":
                message = analyse_total_number("message")
                print(message)
            elif chosen_analyzation == "Get total number of specific file type":
                message = analyse_content_types("message")
                print(message)
            elif chosen_analyzation == "Get day with most files on desktop":
                message = analyse_day_most_files("message")
                print(message)
            # The most common file type ever to clutter your desktop
            elif chosen_analyzation == "Get most common file type":
                message = analyse_most_common_filetype("message")
                print(message)                
            chosen_analyzation = ask_user_options(inq_name, question, choices)
    inq_name = "choose_option"
    question = "What would you like to do?"
    choices = ["Count files on desktop", "Analyse Data", "Quit"]
    user_input = ask_user_options(inq_name, question, choices)
