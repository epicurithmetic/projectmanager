# This file initialises the database for keeping track of the progress on
# my coding projects. Also provides the functions used to connect to the database. 
import sqlite3

def CreateConnection(db_file):

    """
        This function creates a connection with a .db database file.

        If the file does not exist in the directory, then the .db file
        will be created when this function is called.

    """

    # Initialise the connection object.
    conn = sqlite3.connect(db_file)

    return conn

def CreateTable(conn, create_table_sql):

    """
        This function uses the SQL from the second input, to insert a table
        into the database specified by the connection object.

    """

    cur = conn.cursor()
    cur.execute(create_table_sql)


if __name__ == "__main__":

    # Initialise the connection to the CodeProject database.
    database = "CodeProjects.db"
    conn = CreateConnection(database)

    # Table 1: project name and details
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Projects
                                (id integer PRIMARY KEY,
                                Project text NOT NULL,
                                Description text NOT NULL,
                                State text NOT NULL
                                );"""

    # Table 2: Steps for specific project.
    sql_create_steps_table = """ CREATE TABLE IF NOT EXISTS Steps
                             (id integer PRIMARY KEY,
                             Name text NOT NULL,
                             Project text NOT NULL,
                             ParentStep text,
                             Description text NOT NULL,
                             State text NOT NULL
                             );"""

    # Insert these tables into the CodeProjects database.
    CreateTable(conn,sql_create_projects_table)
    CreateTable(conn,sql_create_steps_table)

    # Close the connection to the database.
    conn.close()
