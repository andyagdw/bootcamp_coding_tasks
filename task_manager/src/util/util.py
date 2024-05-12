'''This module defines utiliy functions'''

import datetime


def convert_date(date_string) -> datetime.date:
    '''
    Takes in a string in this format (%m-%d-%Y) and converts it into
    <class 'datetime.date'>. It then returns the new_date
    '''
    new_date = datetime.datetime.strptime(date_string, "%m-%d-%Y").date()
    return new_date


def full_date() -> datetime.date:
    '''Returns the current date in this format: year-month-day'''
    todays_date = datetime.date.today()
    return todays_date
