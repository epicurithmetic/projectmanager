# Project manager console.
import os
import sqlite3
from PMconsole_library import HomeScreen
from PMconsole_library import LookUp
from PMconsole_library import Close


if __name__ == "__main__":

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
            # In this case, there are no options, so we can simply give the
            # content the user has asked for.
            if user_state.option == "read":
                user_state.content()

        # At this point the user has chosen an option. We need to act on the option
        # But this action depends on the state of the user i.e. where they are in the console.
        if user_state.state == "Home":

            # In this case, the user has chosen an option on the HomeScreen()
            if user_option == "L":
                user_state = LookUp()
            else:
                user_state = Close()

        # For now, just close the console. Adjust this when other parts of the
        # console have been written.
        else:
            user_state = Close()
