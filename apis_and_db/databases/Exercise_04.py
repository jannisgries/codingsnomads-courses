'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


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

# Engine Object
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:dewrEg-sumden-degde6@localhost/employees', isolation_level="AUTOCOMMIT")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Variables for script
chosen_task = ""
horizontal_line = "__________________________________________"
active_table = ""
insp = sqlalchemy.inspect(engine)
column_names = ""


##############################################################
# Function Definitions
##############################################################

##############################################################
# General functions
def wait_for_user():
    """Force User to press Enter in order to continue
    """
    while True:
        user_input = input("\nPress Enter to choose next option: ")
        if user_input == "":
            break
        else:
            print("Please press enter only.")
    print(f"\n{horizontal_line}\n")

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

def choose_active_table():
    """Choose an active table out of the list of db tables

    Returns:
        string: name of chosen table
    """
    tables = insp.get_table_names()
    if tables == []:
        print("There are currently no tables in your database.")
        chosen_table = ""
    else:
        inq_name = "tables"
        question = "Which table would you like to choose? "
        choices = tables
        chosen_table = ask_user_options(inq_name, question, choices)
    return chosen_table

def get_active_table(active_table):
    """Get the Table Element of the active Table

    Args:
        active_table (string): Name of currently active table

    Returns:
        string: Name of currently active table,
        SQLAlchemyTableElement: Active Table as Table Element

    """
    if active_table == "":
        active_table = choose_active_table()
    # Create query
    table = sqlalchemy.Table(active_table, metadata, autoload_with=engine)
    return active_table, table

def get_column_names():
    """Get all the columns of the current table
    Returns:
        list: Name of collumsn
    """
    query = sqlalchemy.select(table)
    result = connection.execute(query)
    column_names = []
    for r in result.keys():
        column_names.append(r)
    return column_names

##############################################################
# Interact with User // Locic of Programme
##############################################################

while chosen_task != "QUIT":
    ##############################################################
    # Ask User for Task, which he would like to do
    inq_name = "action"
    question = "What would you like to do?"
    choices = ["1) Create new Table",
               "2) Show all Tables of DB",
               "3) Change active Table",
               "4) Show Column-Names of Table",
               "5) Select Data from Table",
               "6) Insert Data into Table",
               "7) Update Data in Table",
               "8) Delete Data from Table",
               "9) Delete Table from DB",
               "QUIT"]

    chosen_task = ask_user_options(inq_name, question, choices)
    ##############################################################
    # Create New Table
    if chosen_task == "1) Create new Table":
        # Ask general information about the table, which should be created
        table_name = input("What should be the name of the table?: ")
        columns = []
        num_of_columns = int(
            input("How many columns should this table have?: "))
        print(horizontal_line)
        primary_key_chosen = False
        # Ask for each column additional information
        for num in range(1, num_of_columns + 1):
            ##############################################################
            # Name
            column_name = input(
                f"What should be the name of the {num}. column?: ")

            ##############################################################
            # Ask for Primary Key
            if primary_key_chosen == False:
                inq_name = "primary_key"
                question = "Should this column be the primary key?"
                choices = ["Yes", "No"]
                primary_key_choice = ask_user_options(
                    inq_name, question, choices)
                if primary_key_choice == "Yes":
                    primary_key = True
                    primary_key_chosen = True
                else:
                    primary_key = False
            else:
                primary_key = False

            ##############################################################
            # Type
            inq_name = "column_type"
            question = "Which type should the data of this column be?: "
            choices = ["Integer",
                       "String",
                       "Float",
                       "Boolean"
                       ]
            column_user_input = ask_user_options(inq_name, question, choices)
            if column_user_input == "Integer":
                column_type = sqlalchemy.Integer()
            elif column_user_input == "String":
                column_type = sqlalchemy.String(255)
            elif column_user_input == "Float":
                column_type = sqlalchemy.Float()
            elif column_user_input == "Boolean":
                column_type = sqlalchemy.Boolean()

            ##############################################################
            # Nullable
            if primary_key != True:
                inq_name = "column_nullable"
                question = "Should this column be nullable?"
                choices = ["Yes (Nullable)",
                           "No (Not Nullable)"
                           ]
                user_input = ask_user_options(inq_name, question, choices)
                if user_input == "No (Not Nullable)":
                    nullab = False
                elif user_input == "Yes (Nullable)":
                    nullab = True
            else:
                nullab = False
            ##############################################################
            # Default Value
            inq_name = "column_default"
            question = "Should there be a default value?"
            choices = ["Yes",
                       "No"
                       ]
            user_input = ask_user_options(inq_name, question, choices)
            if user_input == "Yes":
                default_value = input("Please type in the default value: ")
            elif user_input == "No":
                default_value = None
            ##############################################################
            # Add column to table
            columns.append(sqlalchemy.Column(f'{column_name}', column_type, primary_key=primary_key,
                           nullable=nullab, server_default=default_value, default=default_value))
        # Add Table to DB
        newTable = sqlalchemy.Table(table_name, metadata, *columns)
        metadata.create_all(engine)
        insp = sqlalchemy.inspect(engine)

    ##############################################################
    # Show all Tables from DB
    elif chosen_task == "2) Show all Tables of DB":
        # Get Tables von Inspect-Object
        tables = insp.get_table_names()
        if tables == []:
            print("There are currently no tables in your database.")
        else:
            for table in tables:
                print(table)

    ##############################################################
    # Choose/ Change active Table 
    elif chosen_task == "3) Change active Table":
        active_table = choose_active_table()
        # Reset locally stored values of column names
        column_names = ""
        if active_table != "":
            print(f"{active_table} is now the active table.")
    
    ##############################################################
    # Show Column Names of Table
    elif chosen_task == "4) Show Column-Names of Table":
        # Determine active table
        active_table, table = get_active_table(active_table)
        if column_names == "":
            column_names = get_column_names()
        column_names_string = "  ||  ".join(column_names)
        print(column_names_string)

    ##############################################################
    # Select Data from Table
    elif chosen_task == "5) Select Data from Table":
        # Determine active table
        active_table, table = get_active_table(active_table)

        # Ask user, if he wants to get all data from db
        inq_name = "access_attribute"
        question = "Would you like to specify the selection?"
        choices = ["Specify by Value",
                   "Specify by Limit-Number",
                   "No Specification, get all"
                   ]
        user_input = ask_user_options(inq_name, question, choices)
        # Get Column-Names from Table
        if column_names == "":
            column_names = get_column_names()
       
        # Build query
        if user_input == "Specify by Value":          
            # Ask user, which column he wants to give the value to
            inq_name = "select_column"
            question = "By what property would you like to select the data?"
            choices = column_names
            user_input_column = ask_user_options(inq_name, question, choices)
            # Build new query
            user_input_value = input("Which value should the data have?: ")
            query = sqlalchemy.select(table).where(getattr(table.columns, user_input_column) == user_input_value)            
            result = connection.execute(query)
        elif user_input == "Specify by Limit-Number":
            # Ask user, how many columns he wants to grab
            user_input_number = int(input("How many records would you like to retrieve?: "))
            query = sqlalchemy.select(table)
            result = connection.execute(query)
            result = result.fetchmany(user_input_number)
        elif user_input == "No Specification, get all":
            query = sqlalchemy.select(table)
            result = connection.execute(query)
            result = result.fetchall()
        # Print results, ordered by column na,es
        for el in column_names:
            print(el, end=f"{' ' * (10 - len(str(el)))}")
        print()
        for el in result:
            for e in el:
                print(e, end=f"{' ' * (10 - len(str(e)))}")
            print()
    
    ##############################################################
    # Insert (new) Data into Table
    elif chosen_task == "6) Insert Data into Table":
        # Determine active table
        new_records = []
        active_table, table = get_active_table(active_table)
        # Determine Columns of Table
        if column_names == "":
            column_names = get_column_names()
        input_values = []
        more_records = "yes"
        while more_records == 'yes':
            # Ask user for input values
            for column in column_names:
                user_input = input(f"What should the value be for the column {column}?: ")
                input_values.append(user_input)
            # Generate row of values, which is the new entry
            new_record = {column_names[i]: input_values[i] for i in range(len(column_names))}
            # Append new entry to list of entries
            new_records.append(new_record)
            print(horizontal_line)
            more_records = input("Would you like to add more records (Type in 'yes' or 'no')? ")
        # Add all entries to db
        query = sqlalchemy.insert(table)
        result = connection.execute(query, new_records)     
        
    ##############################################################
    # Update Entry
    elif chosen_task == "7) Update Data in Table":
        # Determine active table
        active_table, table = get_active_table(active_table)
        
        # Let user decide, by which way he wants to select the entry, which should be updated
        inq_name = "access_attribute"
        question = "How would you like to select the entry, which values you would like to update?"
        choices = ["Specify by Primary Key",
                   "Choose from all Entries"
                   ]
        user_input = ask_user_options(inq_name, question, choices)
        # Get primary key of table
        for pk in table.primary_key:
            table_pk = pk
        # Let User decide, which entry he wants to update
        if user_input == "Specify by Primary Key":        
            pk_uservalue = input(f"What is the value of the row to be changed with regard to the primary key '{table_pk.name}'?")
        elif user_input == "Choose from all Entries":
            inq_name = "choose_entry"
            question = "Which entry would you like to update?"
            choices = []
            query = sqlalchemy.select(table)
            result = connection.execute(query)
            for el in result.mappings():
                choices.append(el)
            user_input = ask_user_options(inq_name, question, choices)
            chosen_entry = dict(user_input)
            pk_uservalue = chosen_entry[table_pk.name]
        # Ask User, which column entry he would like to update
        input_values = []
        if column_names == "":
            column_names = get_column_names()
        changeable_columns = column_names   
        inq_name = "choose_column"
        question = "Which property would you like to change?"
        choices = changeable_columns
        column_to_change = ask_user_options(inq_name, question, choices)
        # Ask for new value
        new_value = input(f"What should the new value be for the column '{column_to_change}'?: ")
        # Create and execute query
        query = sqlalchemy.update(table).where(table_pk == pk_uservalue).values({column_to_change:new_value})
        result = connection.execute(query)

    ##############################################################
    # Delete Entry
    elif chosen_task == "8) Delete Data from Table":
          # Determine active table
        active_table, table = get_active_table(active_table)
        
        # Let user decide, by which way he wants to select the entry, which should be deleted
        inq_name = "access_attribute"
        question = "How would you like to select the entry, which values you would like to delete?"
        choices = ["Specify by Primary Key",
                   "Choose from all Entries"
                   ]
        user_input = ask_user_options(inq_name, question, choices)
        for pk in table.primary_key:
            table_pk = pk
        # Let User decide, which entry he wants to delete
        if user_input == "Specify by Primary Key":        
            pk_uservalue = input(f"What is the value of the row to be deleted with regard to the primary key '{table_pk.name}'?")
        elif user_input == "Choose from all Entries":
            inq_name = "choose_entry"
            question = "Which entry would you like to delete?"
            choices = []
            query = sqlalchemy.select(table)
            result = connection.execute(query)
            for el in result.mappings():
                choices.append(el)
            user_input = ask_user_options(inq_name, question, choices)
            chosen_entry = dict(user_input)
            pk_uservalue = chosen_entry[table_pk.name]
        # Query to delete selected entry
        query = sqlalchemy.delete(table).where(table_pk == pk_uservalue)
        result = connection.execute(query)

    ##############################################################
    # Delete Table
    elif chosen_task == "9) Delete Table from DB":
        # Choose Table, which should be deleted
        table_to_delete = choose_active_table()
        table = sqlalchemy.Table(table_to_delete, metadata, autoload_with=engine)
        # Confirm deletion of table
        inq_name = "delete_confirmation"
        question = f"Are you sure, to delete the table {table_to_delete}?"
        choices = ["Yes",
                   "No"
                   ]
        delete_confirmation = ask_user_options(inq_name, question, choices)
        if delete_confirmation == "Yes":
            table.drop(engine)
            insp = sqlalchemy.inspect(engine)

    ##############################################################
    # Quit Programme
    if chosen_task != "QUIT":
        wait_for_user()
