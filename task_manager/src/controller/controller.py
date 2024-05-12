'''This module contains the controller (i.e., the start_application
function). It recieves user input from the views, interacts with the
models to process the input, and updates the views accordingly.
'''

from model import model
from views import views


def start_application(tasks: list) -> list[model.Task] | None:
    '''
    Allows a user to perform actions on the tasks list
    '''
    try:
        user_choice = views.display_menu()
    except ValueError:  # Catch inputs that are not integers
        views.incorrect_input()
        return start_application(tasks)

    match user_choice:
        case 1:  # View tasks
            # Check if there are tasks in the tasks list
            if tasks:
                views.view_tasks(tasks)
            else:
                # Informs the user that there are no tasks
                views.no_tasks()
        case 2:  # Create new task
            try:
                # Returns task information
                task_info = views.get_task_information()
            # Catch any incorrect inputs
            except ValueError:
                views.incorrect_input()
                return start_application(tasks)
            new_task = model.create_task(task_info)
            model.add_task(new_task, tasks)
            views.task_added()
        case 3:  # Remove a task
            if tasks:
                try:
                    task_id = views.get_task_id_to_remove_task()
                # Catch inputs that are not integers
                except ValueError:
                    views.incorrect_input()
                    return start_application(tasks)
                task_to_be_removed = model.search_for_task(task_id, tasks)
                if task_to_be_removed is not None:
                    if views.confirm_choice() == "Y":
                        model.remove_task(task_to_be_removed, tasks)
                        views.task_removed_successfully()
                    else:
                        views.operation_cancelled()
                else:
                    views.task_does_not_exist()
            else:
                views.no_tasks()
        case 4:  # Update a task
            if tasks:
                try:
                    task_id = views.get_task_id_to_update_task()
                # Catch inputs that are not integers
                except ValueError:
                    views.incorrect_input()
                    return start_application(tasks)
                task_to_be_updated = model.search_for_task(
                    task_id, tasks)
                if task_to_be_updated is not None:
                    try:
                        new_task_details = views.get_task_information()
                    # Catch incorrect inputs
                    except ValueError:
                        views.incorrect_input()
                        return start_application(tasks)
                    model.update_task(new_task_details,
                                      task_to_be_updated, tasks)
                    views.task_updated()
                else:
                    views.task_does_not_exist()
            else:
                views.no_tasks()
        case 5:  # View a task
            if tasks:
                try:
                    task_id = views.get_task_id_to_view_task()
                # Catch inputs that are not integers
                except ValueError:
                    views.incorrect_input()
                    return start_application(tasks)
                task_to_be_viewed = model.search_for_task(task_id, tasks)
                if task_to_be_viewed is not None:
                    views.view_task(task_to_be_viewed)
                else:
                    views.task_does_not_exist()
            else:
                views.no_tasks()
        case 6:  # View priorities
            if tasks:
                tasks_sorted_by_priority = model.get_tasks_priorities(tasks)
                views.view_priorities(tasks_sorted_by_priority)
            else:
                views.no_tasks()
        case 7:  # View categories
            if tasks:
                tasks_sorted_by_category = model.get_tasks_categories(tasks)
                views.view_categories(tasks_sorted_by_category)
            else:
                views.no_tasks()
        case 8:  # View deadlines
            if tasks:
                tasks_sorted_by_deadline = model.get_tasks_deadlines(tasks)
                views.view_deadlines(tasks_sorted_by_deadline)
            else:
                views.no_tasks()
        case 9:
            views.exit_application()
            return None
        case _:
            views.incorrect_input()
            return start_application(tasks)

    return start_application(tasks)
