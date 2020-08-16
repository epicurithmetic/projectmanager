# This script contains the classes used to keep track of the state in the
# Project Manager console, as the user changes their needs from the database.


# Classes are used to keep track of the different states the console can be in.
class HomeScreen():

    """
        This class provides the parameters for the homescreen of the
        project manager console.


    """

    def __init__(self):

        """
            This class is used to define the homescreen of the project
            manager console. This class stores the options available to the
            user at the homescreen.

        """

        self.state = "Home"
        self.option = ""

    def header(self):

        """
            This method prints a welcome header for the console home page.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        welcome_message = " Welcome to the Project Manager Console "
        l_welcome = len(welcome_message)

        print(x + 205*y + x)
        print(3*w)

        print(z*75 + x + l_welcome*y + x)
        print(z*75 + x + welcome_message + x)
        print(z*75 + x + l_welcome*y + x)


    def explanation(self):

        """
            This method provides the user with an explanation of the
            program manager and how it can be used.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        explanation_message_1 = z*10 + "This console can be used to access the code project database."
        explanation_message_2 = z*10 + "The user may write, read, and update projects in the database."
        print(w*3)
        print(explanation_message_1)
        print(explanation_message_2)

    def options(self):

        # shortcuts for aesthetic use.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        prompt = "Which of the following options would you like to perform?"

        option_l = "[L]: Look up a project."
        option_u = "[U]: Update a project."
        option_i = "[I]: Insert a new project or step in a project."
        option_r = "[R]: Remove a project."
        option_q = "[Q]: Quit the console."
        #option_h = "[H]: Return to the homescreen."

        options = [option_l,
                   option_u,
                   option_i,
                   option_r,
                   option_q]

        # Start printing the options for the user.
        print(w*2)
        print(z*15 + prompt + w)
        for o in options:
            print(z*20 + o)

        print(w)
        user_option = input(z*15 + "Option: ")

        return user_option



    def continue_program(self):

        """
            This method is used to keep track of whether or not the user
            is finished accessing the database and wishes to close the console.

        """

        return True




class Close():

    """
        This class is used to close the program and print an exit statement.

    """

    def header(self):

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        exit_message = " Thank you for visiting the Project Manager console."
        l_exit = len(exit_message)

        print(x + 205*y + x)
        print(3*w)

        print(z*75 + x + l_exit*y + x)
        print(z*75 + x + exit_message + x)
        print(z*75 + x + l_exit*y + x)

    def continue_program(self):

        """
            This method is used to determine whether or not the user is finished
            and hence that the MAP console should close.

        """

        return False