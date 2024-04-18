#!/user.bin.env python3

"""
This data validator will read input.csv and validate valid data and send it to valid.csv and send any invalid data to
invalid.csv.

The data validator will check for:
    C = Invalid data element count
    I = Invalid id that isn't an integer
    N = Invalid names that are not in a "last name, first name" format
    E = Invalid email that are not in proper email format or not .edu extension
    P = Invalid phone numbers that are not in a 111-222-3333 format
    D = Invalid date that are not in a MM/DD/YYYY format
    T = Invalid time that are not in a HH:MM military format

A report will be displayed to show how many records validated successfully along with an error report of each invalid
data type from above.
"""

__author__ = 'Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/16/2024'
__status__ = 'Development'

import csv
import re


def validate_id(id):
    # regex [0-9]?
    # if re.compile(regex, id):
    #    return
    pass


def validate_name(name):
    # last, first
    pass


def validate_email(email):
    # need @ and .edu
    pass


def validate_phone(phone):
    # 111-222-3333
    pass


def validate_date(date):
    # MM/DD/YYYY
    pass


def validate_time(time):
    # HH:MM military
    pass


def process_file():
    with open("input.csv", newline='') as input_file, \
         open("valid.csv", 'w', newline='') as valid_file, \
         open("invalid.csv", 'w', newline='') as invalid_file:
        input_reader = csv.reader(input_file, delimiter='|')
        valid_writer = csv.writer(valid_file, delimiter=',')
        invalid_writer = csv.writer(invalid_file, delimiter='|')

        for line in input_reader:
            valid_writer.writerow(line)


if __name__ == '__main__':
    process_file()

