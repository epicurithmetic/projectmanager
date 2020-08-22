# Project manager console.
import os
import sqlite3

# Load in the classes required to define the different modules of the console.
from PMconsole_library import HomeScreen
from PMconsole_library import LookUp
from PMconsole_library import InsertData
from PMconsole_library import Close

# Load in the functions required to write and read data.
from write_database import InsertProject
from write_database import InsertStep

# Some defintions for creating readable output.
x = "|||"
y = "-"
z = " "
w = "\n"

if __name__ == "__main__":

    # Check if the database exists. If it does, then pass through.
    # Otherwise run the create_database.py file to create the database
    # for this console to interact with.

    # Provide a connection to the database.
    conn = sqlite3.connect("CodeProjects.db")

    # Provide the initial state of the user.
    user_state = HomeScreen()

    while user_state.continue_program() == True:

        os.system("clear")

        # Print the main screen information.
        user_state.header()
        user_state.explanation()

        # If there are options, then present them to the user.
        if user_state.option == "":
            user_option = user_state.options()
        else:
            # In this case there are no options to present, as the user has
            # already specified what they want to see.
            if user_state.option == "read":
                user_state.content()

                # Once the content has been given, we can output the
                # option for where the user wants to go next and update
                # the state, ready for the piece of code.

        # At this point the user has chosen an option. We need to act on the option
        # But this action depends on the state of the user i.e. where they are in the console.
        if user_state.state == "Home":

            # In this case, the user has chosen an option on the HomeScreen()
            if user_option == "L":
                user_state = LookUp()
            elif user_option == "I":
                user_state = InsertData()
            else:
                user_state = Close()


        # In this case, the user has chosen an option on the InsertData() module.
        elif user_state.state == "InsertData":

            if user_option == "P":
                # The user wants to write a new project.
                continue_writing = True                     # Loop until all projects written.
                while continue_writing == True:
                    print(w*2)
                    InsertProject(conn)
                    print(w)
                    user_continue = input("Would you like to write more projects? [Y/n] ")
                    if user_continue == "n":
                        continue_writing = False
                        user_state = HomeScreen()           # Once projects are written
                    else:                                   # User is retured to HomeScreen()
                        pass

            elif user_option == "S":
                # The user wants to write a new step.
                continue_writing = True                     # Loop until all steps written.
                while continue_writing == True:
                    print(w*2)
                    InsertStep(conn)
                    print(w)
                    user_continue = input("Would you like to write more steps? [Y/n] ")
                    if user_continue == "n":
                        continue_writing = False
                        user_state = HomeScreen()           # Once steps are written
                    else:                                   # User is retured to HomeScreen()
                        pass

            elif user_option == "H":
                # In this case, the user wants to return to the homescreen.
                user_state = HomeScreen()

            else:
                # Otherwise, the user wants to quit the console.
                user_state = Close()

        # For now, just close the console. Adjust this when other parts of the
        # console have been written.
        else:
            user_state = Close()
