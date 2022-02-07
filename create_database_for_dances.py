import pymysql
import getpass
from steps import *

#   - use the connection in the parameters to create a cursor
#   - use the cursor, to execute SQL statements
#   - call connection.commit() to save changes you make to the database
#

def reset_database(connection):
    """
    this method creates tables. if the tables already exist, drop them first.

    returns: None
    """
   
    
    # , query1, query2, statement]
    query0 = 'DROP TABLE IF EXISTS dances, steps;' #insert table names here
    query1 = """CREATE TABLE dances (
        name VARCHAR(255) NOT NULL,
        danceId bigint(20) NOT NULL AUTO_INCREMENT,
        moves JSON,
        PRIMARY KEY ('danceId)

    ); """ 
    
    # joint1 JSON will be [angle, time]   
    query2 = """CREATE TABLE steps (
        name VARCHAR(255), 
        stepId bigint(20) NOT NULL AUTO_INCREMENT,
        joint1 JSON, 
        joint2 JSON, 
        joint3 JSON, 
        joint4 JSON, 
        joint5 JSON, 
        joint6 JSON, 
        joint7 JSON, 
    );"""

    queries = [query0, query1, query2]
    statement = "INSERT INTO geekstudent( id, name,gender, subject)\
VALUES(6,'Shoit','M', 'ML')"
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
   
    cursor.close()
    connection.commit()
    
    return 

def fill_db():
    for step in dance_step_database:
        print(step)



def insert_step(name, angle1, angle2, angle3, angle4, angle5, angle6, angle7): #insert attributes
    """
    insert a new row into the table using the parameters given. you don't
    need to input the petID column, but you MUST use %s for the other columns.

    returns: None
    """
    query = 'INSERT INTO steps VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor = connection.cursor()
    cursor.execute(query, (name, angle1, angle2, angle3, angle4, angle5, angle6, angle7))
    cursor.close()
    connection.commit()

#main method to execute
def main():
    ##change database to name of database
    
    database = 'Forest'
    user_password = getpass.getpass(prompt = 'Enter Password: ')
    global connection
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=user_password,
                                 db= None,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.Cursor)

    cursor = connection.cursor()

    # cursor.execute("CREATE DATABASE Forest;")
    cursor.execute("USE Forest;")


    ###creates tables
    #*****UNCOMMENT TO RESET DATABASE********8
    reset_database(connection)

    # insert_step(connection, "ISO_LEFT", 0, 0, 20, 0, 45, 0, 0)

    ###

    # print(cursor.fetchall())

    ###
    

    connection.close()

if __name__ == "__main__":
    main()
