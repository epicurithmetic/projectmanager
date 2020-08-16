# This script contains functions used to read the Project manager database
# and present the projects and steps (of steps etc.) in a clear and readable
# manner.
import os
import sqlite3

conn = sqlite3.connect("CodeProjects.db")

def ProjectManagerProjects(conn):

    """
        This function returns a list of all the projects in the
        CodeProjects.db database.

    """

    # This is the SQL command to grab the names of the projects.
    sql_projects = "SELECT Project FROM Projects"

    # Set the cursor on the database and execute the command.
    cur = conn.cursor()
    cur.execute(sql_projects)

    # Collate the results from the command.
    projects = cur.fetchall()
    number_of_projects = len(projects)      # Clean format into strings.
    for i in range(0,number_of_projects):   # Rather than the native set format.
        projects[i] = projects[i][0]

    return projects

def ProjectSteps(project,conn):

    """
        This function returns, for a given project name, all of the steps in the
        database that are required to complete the project.

    """

    # This is the SQL command to get the steps for the input project.
    sql_steps = ("SELECT Name FROM Steps WHERE Project = '%s';" % project)

    # Set the cursor on the database and execute the command
    cur = conn.cursor()
    cur.execute(sql_steps)

    # Collate the results from the command
    steps = cur.fetchall()
    number_of_steps = len(steps)        # Clean the format of the output.
    for i in range(0,number_of_steps):  # Avoiding set notation.
        steps[i] = steps[i][0]


    return steps

def ProjectWithTopSteps(project,conn):

    """


    """

    # SQL command
    sql_top_steps = ("SELECT Name FROM Steps WHERE Project = '%s' AND ParentStep = 'Top';" % project)
    # Set the cursor on the database and execute the command.
    cur = conn.cursor()
    cur.execute(sql_top_steps)

    # Collate the results
    top_steps = cur.fetchall()
    number_of_top_steps = len(top_steps)
    for i in range(0,number_of_top_steps):
        top_steps[i] = top_steps[i][0]

    project_with_top_steps = [project,top_steps]

    return project_with_top_steps


def DependentSteps(step,conn):

    """


    """

    # SQL command.
    sql_dependent_steps = ("SELECT Name FROM Steps WHERE ParentStep = '%s'" % step)

    # Set the cursor on the database and execute the command.
    cur = conn.cursor()
    cur.execute(sql_dependent_steps)

    # Collate and clean the results.
    dependent_steps = cur.fetchall()
    number_of_dependent_steps = len(dependent_steps)
    for i in range(0,number_of_dependent_steps):
        dependent_steps[i] = dependent_steps[i][0]

    return dependent_steps

def ProjectsNestedSteps(conn):

    """
        Rewrite this into two functions. One of which does this
        for a single project. The other calls the former function
        for each project.

    """

    # Grab all of the projects.
    projects = ProjectManagerProjects(conn)

    # Initialize the final list.
    projects_with_main_steps = []
    for project in projects:

        # Initialize the list with all of the steps for the project.
        project_with_nested_steps = [project]

        # Grab all of the top steps of the project.
        project_with_top_steps = ProjectWithTopSteps(project,conn)
        top_steps = project_with_top_steps[1]

        for step in top_steps:
            # For each top step, grab the dependent steps.
            sub_steps = DependentSteps(step,conn)
            nested_steps = [step, sub_steps]                # Collate the data.
            project_with_nested_steps.append(nested_steps)  # Append to output.

        # Append project with step dependencies to the output data.
        projects_with_main_steps.append(project_with_nested_steps)

    return projects_with_main_steps

def PrintProjectsData(conn):

    """
        Again, rewrite this into two functions. One which prints the data
        of a single project. The other which calls the former to print
        the data of all projects.

    """

    # Collect all of the project data, with nested step dependencies.
    ProjectData = ProjectsNestedSteps(conn)
    number_of_projects = len(ProjectData)

    # Indent for printing.
    indent = 5

    # Empty or cross.
    finished = "[X]: "
    not_finished = "[ ]: "

    for project in ProjectData:

        # Print the project name.
        print(" "*indent + "[ ]: " + project[0])

        # Move onto the steps.
        for step in project[1:]:

            # Print the step name.
            print(" "*(indent + 5) + "[ ]: " + step[0])

            for sub_step in step[1]:
                print(" "*(indent + 10) + "[ ]: " + sub_step)

        print("\n")

    return None








PrintProjectsData(conn)
