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


def insert_step(step_name, *joints):  # insert attributes
    """
    insert a new row into the table using the parameters given. you don't
    need to input the petID column, but you MUST use %s for the other columns.
    returns: None
    """
    cursor = connection.cursor()
    addStep = """INSERT INTO `steps` (name, joint1, joint2, joint3, joint4, joint5, joint6, joint7) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(addStep, (step_name, *joints))
    cursor.close()
    connection.commit()

# main method to execute


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
