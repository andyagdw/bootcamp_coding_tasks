'''Unit testing the use case: add deadline'''

import unittest  # Built in testing framework
import datetime
from src.util import util
from src.model import model


class TestAddDeadline(unittest.TestCase):
    '''
    A unit test class which inherits from unittest.Testcase.
    It contains one test case, which tests the use case:
    add deadline to a task
    '''
    def setUp(self) -> None:
        '''
        Creates task information and a Task instance before
        each test
        '''
        self.task_title = "Coding task"
        self.task_description = "Submit task 1"
        self.task_category = "personal"
        self.task_deadline = util.convert_date('1-01-2030')
        self.task_priority = 1

        self.task = model.create_task([self.task_title,
                                      self.task_description,
                                      self.task_category,
                                      self.task_deadline,
                                      self.task_priority]
                                      )

    def tearDown(self) -> None:
        '''
        Sets current_task_id back to 1
        '''
        model.Task.current_task_id = 1

    def test_deadline_class_was_added_to_task(self):
        '''Tests if deadline class was added to task'''
        self.assertTrue(isinstance(self.task.deadline, model.Deadline))

    def test_deadline_value_is_type_datetime_date(self):
        '''
        Tests if deadline value is of correct type
        '''
        self.assertTrue(
            isinstance(self.task.deadline.deadline, datetime.date)
            )


# Invoke unit test framework
if __name__ == "__main__":
    unittest.main()
