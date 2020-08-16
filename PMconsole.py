# Project manager console.
import os
from PMconsole_library import HomeScreen
from PMconsole_library import Close


if __name__ == "__main__":

    user_state = HomeScreen()


    while user_state.continue_program() == True:

        os.system("clear")

        # Print the main screen information.
        user_state.header()
        user_state.explanation()

        # Present the options to the user.
        user_state.options()

        user_state = Close()
