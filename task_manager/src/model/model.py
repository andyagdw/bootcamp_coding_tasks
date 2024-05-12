'''
This module contains the models.
They represent the application's software entities and business logic.
They get and manipulate data from the database
'''

import datetime
from datetime import date


class Category:
    '''A class to represent a category name'''

    def __init__(self, name: str) -> None:
        self.name = name.title()

    def __str__(self) -> str:
        '''Returns a category name'''
        return f"Category: {self.name.title()}"


##########################
class Priority:
    '''A class to represent a priority level'''

    def __init__(self, priority: int) -> None:
        self.priority = priority

    def __str__(self) -> str:
        '''Returns a priority level'''
        return f"Priority: {self.priority}"


##########################
class Deadline:
    '''A class to represent a date'''

    def __init__(self, deadline: datetime.date) -> None:
        self.deadline = deadline

    def __str__(self) -> str:
        '''Returns a date'''
        return f"Deadline: {self.deadline}"


##########################
class Task:
    '''A class to represent a task'''

    current_task_id = 1

    def __init__(self,
                 title: str,
                 description: str,
                 category: Category,
                 deadline: Deadline,
                 priority_id: Priority) -> None:

        self.title = title.title()
        self.description = description.title()
        self.category = category
        self.deadline = deadline
        self.priority_id = priority_id

        self.task_id = Task.current_task_id
        Task.current_task_id += 1

    def __str__(self) -> str:
        '''Returns all the information about a task'''
        return (
            f"Task Id: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"{self.category}\n"
            f"{self.deadline}\n"
            f"{self.priority_id}\n"
        )


##########################
def add_task(new_task: Task, tasks: list) -> list:
    '''
    Takes in a new task and the tasks list, adds the new task to the
    tasks list, and returns the tasks list to the controller
    '''
    tasks.append(new_task)
    return tasks


def create_task(task_information: list) -> Task:
    '''
    Receives task information and creates a new task. It then returns
    the new task to the controller
    '''
    title, description, category, deadline, priority = task_information

    new_task = Task(
        title,
        description,
        Category(category),
        Deadline(deadline),
        Priority(priority)
    )
    return new_task


def search_for_task(task_id: int, tasks: list) -> Task | None:
    '''
    Takes in a task id and tasks list. It then searches for a task.
    If the task is in the task list, it returns the task. Otherwise,
    it returns None to the controller
    '''
    for value in tasks:
        if value.task_id == task_id:
            return value
    return None


def remove_task(task_to_be_removed: Task, tasks: list) -> list:
    '''
    Takes in a task to be removed from the tasks list and the tasks
    lists. It then removes the task and returns the tasks list to the
    controller
    '''
    index = tasks.index(task_to_be_removed)
    tasks.pop(index)
    return tasks


def update_task(task_information: list, task: Task, tasks: list) -> list:
    '''
    Takes in task information, the task to be updated, and the
    tasks list. It updates the task and returns the tasks list to the
    controller
    '''
    title, description, category, _date, priority_id = task_information

    task.title = title
    task.description = description
    task.category = Category(category)
    task.deadline = Deadline(_date)
    task.priority_id = Priority(priority_id)

    return tasks


def get_tasks_priorities(tasks: list) -> dict[int, list]:
    '''
    Takes in the tasks list and groups the tasks by priority level.
    It then returns the priorities_dict to the controller
    '''
    priorities_dict = {1: [], 2: [], 3: []}

    for value in tasks:
        priority = value.priority_id.priority
        priorities_dict[priority].append(value)

    return priorities_dict


def get_tasks_categories(tasks: list) -> dict[str, list]:
    '''
    Takes in the tasks list and groups the tasks by categories.
    It then returns the categories_dict to the controller
    '''
    categories_dict = {}
    for task in tasks:
        category_name = task.category.name
        if category_name not in categories_dict:
            categories_dict[category_name] = [task]
        else:
            categories_dict[category_name].append(task)

    return categories_dict


def get_tasks_deadlines(tasks: list) -> dict[str, list]:
    '''
    Takes in the tasks list and groups the tasks by deadline date.
    It then returns the deadlines_dict to the controller
    '''
    deadlines_dict = {"Today": [], "Tomorrow": [], "Later on": []}

    today = date.today()
    tomorrow = today + datetime.timedelta(days=1)

    for task in tasks:
        if task.deadline.deadline == today:
            deadlines_dict["Today"].append(task)
        elif task.deadline.deadline == tomorrow:
            deadlines_dict["Tomorrow"].append(task)
        else:
            deadlines_dict["Later on"].append(task)

    return deadlines_dict
