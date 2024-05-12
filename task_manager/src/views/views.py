'''
This module contains the views. It is responsible for presenting the
application's data to the user and receiving user input.
'''

from util import util
from util.constants import constants
from model import model


def display_menu() -> int:
    '''
    Presents a menu to the user to perform actions on tasks list.
    It returns an integer (representing the users choice) to the
    controller
    '''
    user_choice = int(
        input(
            '''\nWould you like to:

                    1) View tasks
                    2) Create new task
                    3) Remove a task
                    4) Update a task
                    5) View a task
                    6) View priorities
                    7) View categories
                    8) View deadlines
                    9) Exit application

                    Enter selection: '''
        )
    )
    return user_choice


def view_tasks(tasks: list) -> None:
    '''
    Takes in a list of tasks and prints out all the tasks in
    the tasks list
    '''
    print(" ")
    for task in tasks:
        print(f"{task}\n****************************\n")

    print(f"\nYou have {len(tasks)} task(s) to do\n")


def get_task_information() -> list:
    '''
    Returns a list containing task information (e.g., task title,
    task description) to the controller
    '''
    while True:
        task_title = input("\nWhat is the task title:\n")
        task_description = input("What is the task description:\n")
        task_category = input(
            "What category do you want to put this task in:\n"
            )

        task_date = input(
            "When is the deadline (Please enter in this format: "
            f"'1-01-{util.full_date().year}', as in month-day-year)\n"
            "\tNote: Please ensure that the deadline entered starts "
            "from today onwards:\n"
            )
        task_deadline = util.convert_date(task_date)
        if task_deadline < util.full_date():
            print(
                "\nOops🤔. Please enter a deadline that starts "
                "from today onwards"
                )
            continue

        task_priority = int(input(
            "What is the priority level"
            "\n(1 = High Priority, "
            "2 = Medium Priority, "
            "3 = Low Priority):\n")
                            )
        if task_priority not in {1, 2, 3}:
            print(
                "\nOops🤔. Please enter a priority level that is either "
                "1, 2, or 3"
            )
            continue

        return [
            task_title,
            task_description,
            task_category,
            task_deadline,
            task_priority]


def task_added() -> None:
    '''
    Informs the user that the new task that they have created has been
    successfully added to the tasks list
    '''
    print("\nTask successfully added👍\n")


def get_task_id_to_remove_task() -> int:
    '''
    Gets task id from user to remove a task. It then returns the
    task id to the controller
    '''
    task_id = int(input(
                "\nWhat task do you want to remove: Enter ID:\n")
                )
    return task_id


def task_does_not_exist() -> None:
    '''Informs the user that a task does not exist'''
    print("\nTask does not exist\n")


def confirm_choice() -> str:
    '''
    Gets user choice (to remove a task) from the user and returns
    this choice to the controller
    '''
    user_choice = input(
            "Are you sure you want to remove this task? 'Y' or 'N':\n"
            )
    return user_choice


def task_removed_successfully() -> None:
    '''
    Informs the user that a task has been removed from the tasks
    list
    '''
    print("\nTask has been removed successfully 😁\n")


def get_task_id_to_update_task() -> int:
    '''
    Gets task id from user to update a task. It then returns the
    task id to the controller
    '''
    task_id = int(input(
                "\nWhat task do you want to update? Enter ID:\n")
                  )
    return task_id


def task_updated() -> None:
    '''Inform the user that a task has been updated'''
    print("\nTask has been updated👌\n")


def get_task_id_to_view_task() -> int:
    '''
    Gets user choice (to view a task) from the user and returns
    this choice to the controller
    '''
    task_id = int(input(
                "\nWhat task do you want to view? Enter ID:\n")
                  )
    return task_id


def view_task(task: model.Task) -> None:
    '''Takes in a task and then prints it'''
    print(f'\n{task}')


def view_priorities(priorities_dict: dict[int, list]) -> None:
    '''
    Takes in a dictionary with the following keys (see below). Each key
    contains a list filled with tasks associated with the key

    Tasks are then printed out in descending order -
    from highest priority to lowest priority

    The priority levels are:
    1 (High Priority)
    2 (Medium Priority)
    3 (Low Priority)
    '''
    for priority, priority_task in priorities_dict.items():
        priority_str = (
            "High" if priority == 1
            else ("Medium" if priority == 2 else "Low")
        )
        print(f"\n********* {priority_str} Priority *********")
        if priority_task:  # Check if empty
            for task in priority_task:
                print(
                    f"\n{constants.TASK_ID_STRING}{task.task_id}\n"
                    f"{constants.TASK_TITLE_STRING}{task.title}\n"
                    f"{constants.TASK_DESCRIPTION_STRING}"
                    f"{task.description}\n"
                    f"{task.category}\n"
                    f"{task.deadline}\n"
                )
        else:
            print("No task with this priority\n")


def view_categories(categories_dict: dict[str, list]) -> None:
    '''
    Takes in a dictionary with keys specified by the user. Each key
    contains a list filled with tasks associated with the key

    Tasks are then printed out grouped by their category
    '''
    for category, category_task in categories_dict.items():
        print(f"\n*********** {category} ***********")
        for task in category_task:
            print(
                f"\n{constants.TASK_ID_STRING}{task.task_id}\n"
                f"{constants.TASK_TITLE_STRING}{task.title}\n"
                f"{constants.TASK_DESCRIPTION_STRING}{task.description}\n"
                f"{task.deadline}\n"
                f"{task.priority_id}\n"
            )


def view_deadlines(deadlines_dict: dict[str, list]) -> None:
    '''
    Takes in a dictionary with the following keys (see below). Tasks are
    then printed out grouped by their deadline date

    The categories are:
    Due today
    Due tomorrow
    Due later on
    '''
    for deadline, deadline_task in deadlines_dict.items():
        print(f"\n********* Due {deadline} *********")
        if deadline_task:  # Check if empty
            for task in deadline_task:
                task_info = (
                    f"\n{constants.TASK_ID_STRING}{task.task_id}\n"
                    f"{constants.TASK_TITLE_STRING}{task.title}\n"
                    f"{constants.TASK_DESCRIPTION_STRING}"
                    f"{task.description}\n"
                    f"{task.category}\n"
                    f"{task.priority_id}\n"
                    )
                # Show deadline for dates that are due later on
                if deadline == "Later on":
                    print(f'{task_info}{task.deadline}\n')
                else:
                    print(task_info)
        else:
            print("No tasks due\n")


def no_tasks() -> None:
    '''Informs the user that there are no tasks in the tasks list'''
    print("\nThere are no tasks 😉")


def exit_application() -> None:
    '''Prints to the user to "have a good day"'''
    print("Have a good day👋")


def operation_cancelled() -> None:
    '''Informs the user that an operation has been cancelled'''
    print("\nOperation cancelled\n")


def incorrect_input() -> None:
    '''Informs the user that they have entered an incorrect input'''
    print("\nThere was an error! You have been directed back to the main"
          " screen")
