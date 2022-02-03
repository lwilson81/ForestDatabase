import pymysql
import getpass

#   - use the connection in the parameters to create a cursor
#   - use the cursor, to execute SQL statements
#   - call connection.commit() to save changes you make to the database
#


def reset_database(connection):
    """
    this method creates tables. if the tables already exist, drop them first.

    returns: None
    """
    query0 = 'DROP TABLE IF EXISTS dances, steps;' #insert table names here
    query1 = 'CREATE TABLE dances (name VARCHAR(255) NOT NULL);' #insert columns here
    query2 = 'CREATE TABLE steps (name VARCHAR(255), angle1 int, angle2 int, angle3 int, angle4 int, angle5 int, angle6 int, angle7 int);'
    cursor = connection.cursor()
    cursor.execute(query0)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.close()
    connection.commit()
    
    return 

def insert_step(connection, name, angle1, angle2, angle3, angle4, angle5, angle6, angle7): #insert attributes
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

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password=user_password,
                                 db= database,
                                 charset="utf8mb4",
                                 cursorclass=pymysql.cursors.Cursor)

    cursor = connection.cursor()


    ###creates tables
    #*****UNCOMMENT TO RESET DATABASE********8
    reset_database(connection)

    insert_step(connection, "ISO_LEFT", 0, 0, 20, 0, 45, 0, 0)

    ###

    # print(cursor.fetchall())

    ###
    

    connection.close()

if __name__ == "__main__":
    main()
