# This script contains functions used to read the Project manager database
# and present the projects and steps (of steps etc.) in a clear and readable
# manner.
import os
import sqlite3

conn = sqlite3.connect("CodeProjects.db")

def ProjectIsItFinished(project,conn):

    """
        This function returns True if the project is marked finished in
        the database, otherwise it returns False.

    """

    #rint(project)

    # SQL command to insert.
    sql_state_of_project = "SELECT State FROM Projects WHERE Project = '%s'" % project
    # Set the cursor on the database and execute the command.
    cur = conn.cursor()
    cur.execute(sql_state_of_project)


    state = cur.fetchall()
    state = state[0][0]

    if state == "F":
        return True
    else:
        return False

def StepIsItFinished(step,conn):

    """
        This function returns True if the step is marked finished in
        the database, otherwise it returns False.

    """
    # SQL command to insert.
    sql_state_of_step = "SELECT State FROM Steps WHERE Name = '%s'" % step
    # Set the cursor on the database and execute the command.
    cur = conn.cursor()
    cur.execute(sql_state_of_step)

    state = cur.fetchall()
    state = state[0][0]

    if state == "F":
        return True
    else:
        return False

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

def ProjectNestedSteps(project,conn):

    """
        This function outputs the steps, including nesting, for the input
        project in the CodeProject.db database.

    """

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

    return project_with_nested_steps

def ProjectsNestedSteps(conn):

    """
        This function collects all of the projects, with their nested steps,
        into a single output list.

    """

    # Grab all of the projects.
    projects = ProjectManagerProjects(conn)

    # Initialize the final list.
    projects_with_main_steps = []
    for project in projects:

        # Initialize the list with all of the steps for the project.
        project_with_nested_steps = ProjectNestedSteps(project,conn)
        projects_with_main_steps.append(project_with_nested_steps)

    return projects_with_main_steps

def PrintProjectData(project,conn):

    """


    """

    # Grab the project and its nested step data.
    project = ProjectNestedSteps(project,conn)

    # Indent standard for printing.
    indent = 15
    on_going = "[ ]: "
    finished = "[X]: "

    # Determine whether or not project has been completed:
    isit_finished_project = ProjectIsItFinished(project[0],conn)

    # Printed statement depends on whether finished or not.
    if isit_finished_project == True:
        print(" "*indent + finished + project[0] + "\n")
    else:
        print(" "*indent + on_going + project[0] + "\n")

    # Move onto the steps.
    for step in project[1:]:

        # Determine whether or not the step is finished.
        isit_finished_step = StepIsItFinished(step[0],conn)

        # Printed statement depends on whether the step is finished or not.
        if isit_finished_step == True:
            print(" "*(indent + 5) + finished + step[0])
        else:
            print(" "*(indent + 5) + on_going + step[0])

        for substep in step[1]:

            isit_finished_substep = StepIsItFinished(substep,conn)

            # Printed statement depends on whether the step is finished or not.
            if isit_finished_substep == True:
                print(" "*(indent + 10) + finished + substep)
            else:
                print(" "*(indent + 10) + on_going + substep)

    print("\n")

def PrintProjectsData(conn):

    """


    """

    # Collect all of the project data, with nested step dependencies.
    ProjectData = ProjectsNestedSteps(conn)
    number_of_projects = len(ProjectData)

    for project in ProjectData:

        # Print the project data.
        PrintProjectData(project[0],conn)   # First element in list is the
                                            # name of the project.
    return None
