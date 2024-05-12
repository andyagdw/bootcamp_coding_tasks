'''Unit testing the use case: create task'''

import unittest  # Built in testing framework
from src.util import util
from src.model import model


class TestCreateTask(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.

    It contains one test case, which tests the use case:
    create task
    '''
    def tearDown(self) -> None:
        '''
        Sets current_task_id back to 1
        '''
        model.Task.current_task_id = 1

    def test_if_task_creation_was_success(self) -> None:
        '''
        Tests if task creation was successful
        '''
        # Create a new task
        new_task = model.create_task(["Coding task",
                                      "Submit task 1",
                                      "Personal",
                                      util.full_date(),
                                      1]
                                     )
        # Instances of the Task class are assigned a task id, which
        # increases everytime a new task instance is created
        self.assertEqual(new_task.task_id, 1)


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
