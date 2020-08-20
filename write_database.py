# This script allows us to write to the database of projects.
import os
import sqlite3

# This files contains the functions which are called by the API. These functions
# allow the user to write in NEW projects or steps (of steps of steps...) of
# exisiting projects. For the functions used for updating exisiting projects,
# please see the update_database.py (Which does not yet exist...)

def InsertProject(conn):

    """


    """

    project_name = input("Project name: ")
    project_description = input("Project description: ")
    project_state = input("Project completion state [YTS/OG/F]: ")

    inst_stmt = """ INSERT INTO Projects(Project, Description, State)
                    VALUES(?,?,?)"""

    project_data = (project_name, project_description, project_state)

    # Check that project_name is the name of a project in the database.

    with conn:
        cur = conn.cursor()
        cur.execute(inst_stmt,project_data)

    print("Project details have been inserted into the database.")

def InsertStep(conn):

    """


    """

    step_name = input("Step name: ")
    step_project = input("Parent project: ")
    step_parent = input("Parent step: ")
    step_description = input("Step description: ")
    step_state = input(" Step completion state [YTS/OG/F]: ")

    inst_stmt = """ INSERT INTO Steps(Name,Project,ParentStep,Description,State)
                    VALUES(?,?,?,?,?)"""
    step_data = (step_name, step_project, step_parent, step_description, step_state)

    with conn:
        cur = conn.cursor()
        cur.execute(inst_stmt,step_data)

    print("Step details have been inserted into the database.")
