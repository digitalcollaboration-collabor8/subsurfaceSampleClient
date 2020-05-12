import os
from datetime import datetime, timedelta

def create_filepath_if_not_exists(filepath):
    """
    Creates the given filepath path if not existing
    """
    dirname=os.path.dirname(filepath)
    #check if it exists or not
    if os.path.exists(dirname)==False:
        os.makedirs(dirname)


def create_date_range(days_from_current_day):
    """
    Creates a to from date range based on current day minus number of days incoming
    """
    return substract_days(datetime.today(),days_from_current_day)

def substract_days(date,days):
    return date - timedelta(days=days)

def add_days(date,days):
    return date + timedelta(days=days)

def format_date(date, format):
    """
    Formats a date according to the given format
    """
    return date.strftime(format)

def format_date_to_yy_mm_dd(date):
    return format_date(date,'%Y-%m-%d')