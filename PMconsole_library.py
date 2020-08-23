# This script contains the classes used to keep track of the state in the
# Project Manager console, as the user changes their needs from the database.
import sqlite3
from read_database import PrintProjectsData

# Make a connection to the database.
conn = sqlite3.connect("CodeProjects.db")

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

        option_l = "[L]: Look up the projects."
        option_u = "[U]: Update a project."
        option_i = "[I]: Insert a new project or step into a project."
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

class LookUp():

    """


    """

    def __init__(self):

        """
            This class is used to define the homescreen of the project
            manager console. This class stores the options available to the
            user at the homescreen.

        """

        self.state = "LookUp"
        self.option = ""

    def header(self):

        """
            This method prints a welcome header for the console home page.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        welcome_message = " Project Manager Console: Read Database. "
        l_welcome = len(welcome_message)

        print(x + 205*y + x)
        print(3*w)

        print(z*75 + x + l_welcome*y + x)
        print(z*75 + x + welcome_message + x)
        print(z*75 + x + l_welcome*y + x)


    def explanation(self):

        """


        """

        # Some definitions for "aesthetics".
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        explanation_message_1 = z*10 + "This section of the console allows users read access"
        explanation_message_2 = " to the project manager database."

        print(w*3)
        print(explanation_message_1 + explanation_message_2 + w*2)


    def content(self):

        """


        """

        # Provide the user with the project and steps database.
        PrintProjectsData(conn)

        # Once the content has been given, we need to provide
        # options for the user to continue moving around the console.

    def options(self):

        """
            Options for this class will be given at the bottom of the
            printed database. Rather than as the initial output, as is the
            case with the other modules.

        """

        # shortcuts for aesthetic use.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        prompt = "Which of the following options would you like to perform?"

        option_v = "[V]: View the entire database of code projects"
        option_d = "[D]: View the details of a single project."
        option_h = "[H]: Return to the home screen of the console."
        option_q = "[Q]: Quit the project manager console."

        options = [option_v,
                   option_d,
                   option_h,
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

class InsertData():

    """
        This class is used to implement the code for writing projects
        to the CodeProject.db database.

    """

    def __init__(self):

        """
            This class is used to define the homescreen of the project
            manager console. This class stores the options available to the
            user at the homescreen.

        """

        self.state = "InsertData"
        self.option = ""

    def header(self):

        """
            This method prints the header for the write data section of the
            project manager console.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        welcome_message = " Project Manager Console: Write Data "
        l_welcome = len(welcome_message)

        print(x + 205*y + x)
        print(3*w)

        print(z*75 + x + l_welcome*y + x)
        print(z*75 + x + welcome_message + x)
        print(z*75 + x + l_welcome*y + x)

    def explanation(self):

        """
            This method provides the user with an explanation of the
            types of data that can be written to the project manager
            CodeProjects.db database.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        explanation_message_1 = z*10 + "This module of the console lets the user write data to the CodeProject.db database."
        explanation_message_2 = z*10 + "You may write a project, or a step into a project."
        print(w*3)
        print(explanation_message_1)
        print(explanation_message_2)


    def options(self):

        """

        """

        # shortcuts for aesthetic use.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        prompt = "Choose whether you would like to write a new project or a step into an exisiting project."

        option_p = "[P]: Write a new project."
        option_s = "[S]: Write a new step into a project."
        option_h = "[H]: Return to the home screen."
        option_q = "[Q]: Quit the project manager console."

        options = [option_p,
                   option_s,
                   option_h,
                   option_q]

        # Start printing the options for the user.
        print(w*2)
        print(z*15 + prompt + w)
        for o in options:
            print(z*20 + o)

        print(w)
        user_option = input(z*15 + "Option: ")

        # Update the option attribute of this class.
        self.option = user_option

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

    def __init__(self):

        """
            This class is used to define the homescreen of the project
            manager console. This class stores the options available to the
            user at the homescreen.

        """

        self.state = "Close"
        self.option = ""

    def header(self):

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        exit_message = " Thank you for visiting the Project Manager Console."
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
