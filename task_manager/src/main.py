'''
This module is the main entry point of the application
It imports the start_application function from the controller module,
which starts the task manager application
'''

from controller import controller

# Only call the function when the script is executed directly
if __name__ == "__main__":
    # Initialise the tasks list, which will store all tasks
    tasks_list = []

    controller.start_application(tasks_list)
