'''Unit testing the use case: update task'''

import unittest  # Built in testing framework
import datetime
from src.util import util
from src.model import model


class TestUpdateTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains four test cases, which tests whether the
    'model.update_task()' function correctly updates the task
        1) title
        2) description
        3) deadline
        4) priority
    '''
    def setUp(self) -> None:
        '''
        Creates task information and a Task instance before
        each test
        '''
        self.today_date = util.full_date()
        self.task_title = "Coding task"
        self.task_description = "Submit task 1"
        self.task_category = "personal"
        self.task_deadline = self.today_date
        self.task_priority_id = 1

        self.task = model.Task(self.task_title,
                               self.task_description,
                               model.Category(self.task_category),
                               model.Deadline(self.task_deadline),
                               model.Priority(self.task_priority_id)
                               )
        self.tasks = []

    def tearDown(self) -> None:
        '''
        Sets current_task_id back to 1
        '''
        model.Task.current_task_id = 1

    def test_update_task_title(self) -> None:
        '''
        Tests whether the 'model.update_task()' function correctly
        updates the task title
        '''
        # Add task to tasks list
        model.add_task(self.task, self.tasks)
        new_task_title = "Coding task 1"
        model.update_task(
            [new_task_title,  # Change task title
             self.task_description,
             self.task_category,
             self.task_deadline,
             self.task_priority_id],
            self.task,
            self.tasks
            )

        self.assertTrue(self.task.title == new_task_title)

    def test_update_task_description(self) -> None:
        '''
        Tests whether the 'model.update_task()' function correctly
        updates the task description
        '''
        # Add task to tasks list
        model.add_task(self.task, self.tasks)
        new_task_description = "Submit task 2"
        model.update_task(
            [self.task_title,
             new_task_description,  # Change task description
             self.task_category,
             self.task_deadline,
             self.task_priority_id],
            self.task,
            self.tasks
            )

        self.assertTrue(self.task.description == new_task_description)

    def test_update_task_category(self) -> None:
        '''
        Tests whether the 'model.update_task()' function correctly
        updates the task category
        '''
        # Add task to tasks list
        model.add_task(self.task, self.tasks)
        new_task_category = "coding"
        model.update_task(
            [self.task_title,
             self.task_description,
             new_task_category,  # Change task category
             self.task_deadline,
             self.task_priority_id],
            self.task,
            self.tasks
            )
        # The category class takes in a string and returns a version of
        # the string where each word is titlecased, hence why the new
        # task category name has the attribute title.
        self.assertTrue(
            self.task.category.name == new_task_category.title()
            )

    def test_update_task_deadline(self) -> None:
        '''
        Tests whether the 'model.update_task()' function correctly
        updates the task deadline
        '''
        # Add task to tasks list
        model.add_task(self.task, self.tasks)
        # Get tomorrows date
        new_task_deadline = self.today_date + datetime.timedelta(days=1)
        model.update_task(
            [self.task_title,
             self.task_description,
             self.task_category,
             new_task_deadline,  # Change task deadline
             self.task_priority_id],
            self.task,
            self.tasks
            )

        self.assertTrue(
            self.task.deadline.deadline == new_task_deadline
            )

    def test_update_task_priority(self) -> None:
        '''
        Tests whether the 'model.update_task()' function correctly
        updates the task priority
        '''
        # Add task to tasks list
        model.add_task(self.task, self.tasks)
        new_task_priority = 2
        model.update_task(
            [self.task_title,
             self.task_description,
             self.task_category,
             self.task_deadline,
             new_task_priority],  # Change task priority
            self.task,
            self.tasks
            )

        self.assertTrue(
            self.task.priority_id.priority == new_task_priority
            )


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
