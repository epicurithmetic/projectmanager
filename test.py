# Test the data insertion functions.
from write_database import InsertProject
from write_database import InsertStep
from create_database import CreateConnection

projects_database_conn = CreateConnection("CodeProjects.db")

done = False

while done == False:

    user_input = input("P or S? ")

    if user_input == "P":
        InsertProject(projects_database_conn)
    else:
        InsertStep(projects_database_conn)

    finished = input("Done? [Y/n]: ")
    if finished == "Y":
        done = True
    else:
        pass
