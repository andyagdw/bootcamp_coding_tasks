'''Unit testing the use case: remove task'''

import unittest  # Built-in testing framework
from src.model import model
from src.util import util


class TestRemoveTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains one test case, which tests the use case:
    remove task
    '''
    def setUp(self) -> None:
        '''
        Creates task information and a Task instance before
        each test
        '''
        self.task_title = "Coding task"
        self.task_description = "Submit task 1"
        self.task_category = "personal"
        self.task_deadline = util.full_date()
        self.task_priority = 1

        self.task = model.Task(self.task_title,
                               self.task_description,
                               model.Category(self.task_category),
                               model.Deadline(self.task_deadline),
                               model.Priority(self.task_priority)
                               )
        self.tasks = []

    def tearDown(self) -> None:
        '''
        Sets current_task_id back to 1
        '''
        model.Task.current_task_id = 1

    def test_remove_task_from_tasks_list(self) -> None:
        '''
        Tests whether the 'model.remove_task()' function correctly
        removes a task from the tasks list
        '''
        model.add_task(self.task, self.tasks)
        model.remove_task(self.task, self.tasks)
        self.assertNotIn(self.task, self.tasks)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
