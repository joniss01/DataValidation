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


def validate_id(input_id):
    regex = r'^\d+$'    # checks if each number from start to end of the id to see if it matches a number between [0-9]
    if re.match(regex, input_id):
        return ""
    else:
        return "I"


def validate_name(name):
    names = name.split(',')     # last,first
    if len(names) == 2:
        return ""
    else:
        return "N"


def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:edu)$'    # checks for letters and numbers in a standard email
    if re.match(regex, email):                                # but need @ and .edu to be valid
        return ""
    else:
        return "E"


def validate_phone(phone):
    regex = r'^\d{3}-\d{3}-\d{4}$'          # checks for 3 numbers - 3 numbers - 4 numbers (must have the hyphens)
    if re.match(regex, phone):
        return ""
    else:
        return "P"


def validate_date(date):
    regex = r'^(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])/\d{4}$'          # checks for MM/DD/YYYY format
    if re.match(regex, date):                                          # updated to accept 1-12 months and 0-31 days
        return ""
    else:
        return "D"


def validate_time(time):
    regex = r'^([1]\d|2[0-3]):([0-5]\d)$'       # HH:MM military only allows 00-23 hours and 00-59 minutes to be valid
    if re.match(regex, time):
        return ""
    else:
        return "T"


def process_file():
    with open("input.csv", newline='') as input_file, \
         open("valid.csv", 'w', newline='') as valid_file, \
         open("invalid.csv", 'w', newline='') as invalid_file:
        input_reader = csv.reader(input_file, delimiter='|')
        valid_writer = csv.writer(valid_file, delimiter=',')
        invalid_writer = csv.writer(invalid_file, delimiter='|')

        for line in input_reader:
            error_string = ""
            data_count = len(line)
            if data_count == 6:
                error_string += validate_id(line[0])        # Call the validate_id function
                error_string += validate_name(line[1])      # Call the validate_name function
                error_string += validate_email(line[2])     # Call the validate_email function
                error_string += validate_phone(line[3])     # Call the validate_phone function
                error_string += validate_date(line[4])      # Call the validate_date function
                error_string += validate_time(line[5])      # Call the validate_time function

            if error_string == "":
                if len(line) > 1:
                    names = line[1].split(',')
                    valid_writer.writerow([
                        line[0], names[1].strip(), names[0].strip(),
                        line[2], line[3], line[4], line[5]
                    ])
                else:
                    line.insert(0, "C")
                    invalid_writer.writerow(line)
            else:
                line.insert(0, error_string)
                invalid_writer.writerow(line)


if __name__ == '__main__':
    process_file()

