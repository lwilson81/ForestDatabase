import pymysql
import getpass
from steps import *
import json
# import pprint

#   - use the connection in the parameters to create a cursor
#   - use the cursor, to execute SQL statements
#   - call connection.commit() to save changes you make to the database
#


def reset_database(connection):
    """
    this method creates tables. if the tables already exist, drop them first.
    returns: None
    """

    dropTables = 'DROP TABLE IF EXISTS dances, steps;'  # insert table names here

    createDanceTable = """CREATE TABLE dances (
        name VARCHAR(255) NOT NULL,
        moves varchar(255),
        PRIMARY KEY (name)
    ); """

    # joint1 JSON will be JSON {}
    createStepTable = """CREATE TABLE steps (
        name VARCHAR(255), 
        joints varchar(255), 
        PRIMARY KEY (name)
    );"""

    cursor = connection.cursor()
    for query in [dropTables, createDanceTable, createStepTable]:
        cursor.execute(query)

    cursor.close()
    connection.commit()


def fill_db():
    cursor = connection.cursor()

    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    for step in dance_step_database:
        step_name = namestr(step, globals())[0]
        angles = step[0]
        times = step[1]
        joint_dict = dict()
        joint_dict["angles"] = angles
        joint_dict["times"] = times
        addStep = """INSERT INTO `steps` (name, joints) VALUES(%s, %s)"""
        cursor.execute(addStep, (step_name, json.dumps(joint_dict)))

    cursor.close()
    connection.commit()

def check_valid_step(step_name, joints):
    """
    check if the data input can be a valid step
    """
    # vertical 360, -360 (1, 3, 5, 7)
    # horizontal: others 
    # velocity: 4 and up (180 degrees) 
    # bottom joint (1) all the way dwn: 6 can 't be all the way down 
    # addition of all the joints 


    # joint discontinuitry: 
    # functional steps dance_func 

    pass

def check_valid_dance(dance_name, steps):
    """
    check if the data input can be a valid dance
    """
    passes = False
    return passes

def insert_step(step_name, joints):  # insert attributes
    """
    insert a new row into the table using the parameters given. you don't
    need to input the petID column, but you MUST use %s for the other columns.
    returns: None
    """
    if check_valid_step():
        cursor = connection.cursor()
        addStep = """INSERT INTO `steps` (name, joints) VALUES(%s, %s)"""
        cursor.execute(addStep, (step_name, json.dumps(joints)))
        cursor.close()
        connection.commit()
    else:
        print("Error: not valid step")

def insert_dance(dance_name, steps):
    """
    insert dance
    """
    if check_valid_dance():    
        cursor = connection.cursor()
        addStep = """INSERT INTO `dances` (name, steps) VALUES(%s, %s)"""
        cursor.execute(addStep, (dance_name, json.dumps(steps)))
        cursor.close()
        connection.commit()
    else:
        print("Error: not valid dance!")


def main():
    # change database to name of database

    database = 'Forest'
    user_password = getpass.getpass(prompt='Enter Password: ')
    global connection
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=user_password,
                                 db=None,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.Cursor)

    ############ TO CREATE DATABASE UNCOMMENT THIS SECTION ############
    # cursor.execute("CREATE DATABASE Forest;")
    # cursor.execute("USE Forest;")
    ###################################################################

    ####### TO RESET AND REFILL DATABASE UNCOMMENT THIS SECTION #######
    cursor = connection.cursor()
    cursor.execute("USE Forest;")
    reset_database(connection)
    fill_db()
    ###################################################################

    connection.close()


if __name__ == "__main__":
    main()
