# Project manager console.
import os
import sqlite3

# Load in the classes required to define the different modules of the console.
from PMconsole_library import HomeScreen
from PMconsole_library import LookUp
from PMconsole_library import InsertData
from PMconsole_library import Close

# Load in the functions required to write and read data to the database.
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

        user_state.option = user_state.options()

        # At this point the user has chosen an option. We need to act on the option
        # But this action depends on the state of the user i.e. where they are in the console.
        if user_state.state == "Home":

            # In this case, the user has chosen an option on the HomeScreen()
            if user_state.option == "L":
                user_state = LookUp()             # In the future this can be updated to include
            elif user_state.option == "I":        # more look-up options: single project, description etc.
                user_state = InsertData()
            else:
                user_state = Close()


        # In this case, the user has chosen an option on the InsertData() module.
        elif user_state.state == "InsertData":

            if user_state.option == "P":
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

            elif user_state.option == "S":
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

            elif user_state.option == "H":
                # In this case, the user wants to return to the homescreen.
                user_state = HomeScreen()

            else:
                # Otherwise, the user wants to quit the console.
                user_state = Close()


        elif user_state.state == "LookUp":

            if user_state.option == "V":
                print(w)
                user_state.content()
                # Now the user should be given another set of options.
                # ... at this point we could "pause" waiting for the user to input "ENTER"
                # after which point the user will be returned to the previous options.
                return_message_1 = "When you finished reading the database, "
                return_message_2 = "please press ENTER to return to the previous menu: "

                print(w*2)
                input(z*10 + return_message_1 + return_message_2)

            elif user_state.option == "D":
                print("This part of the console is not ready yet.")
                user_state.option = ""

            elif user_state.option == "H":
                user_state = HomeScreen()

            else:
                user_state = Close()

        # For now, just close the console. Adjust this when other parts of the
        # console have been written.
        else:
            user_state = Close()
