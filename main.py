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

A report will be displayed to show the invalid data types from the input using the letters from above.
"""

__author__ = 'Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/16/2024'
__status__ = 'Development'

import csv
import re


def validate_id(input_id):
    """
    Validates the format of an ID so that it only uses valid numbers between 0-9.
    :param input_id: The ID to be tested.
    :return: An empty string if ID is valid, otherwise return I in invalid.csv.
    """
    regex = r'^\d+$'    # checks if each number from start to end of the id to see if it matches a number between [0-9]
    if re.match(regex, input_id):
        return ""
    else:
        return "I"


def validate_name(name):
    """
    Validates the format of a name so that it is last,first separated by a comma.
    :param name: The name to be tested.
    :return: An empty string if name is valid, otherwise return N in invalid.csv.
    """
    names = name.split(',')     # last,first
    if len(names) == 2:
        return ""
    else:
        return "N"


def validate_email(email):
    """
    Validates the format of an email so that it uses letters, numbers, or symbols, but must contain @ and .edu.
    :param email: The email to be tested.
    :return: An empty string if email is valid, otherwise return E in invalid.csv.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(?:edu)$'    # checks for letters, numbers, or symbols that can be in
    if re.match(regex, email):                                # a standard email but need @ and .edu to be valid
        return ""
    else:
        return "E"


def validate_phone(phone):
    """
    Validates the format of a phone number so that it is XXX-XXX-XXXX.
    :param phone: The phone number to be tested.
    :return: An empty string if phone is valid, otherwise return P in invalid.csv.
    """
    regex = r'^\d{3}-\d{3}-\d{4}$'          # checks for 3 numbers - 3 numbers - 4 numbers (must have the hyphens)
    if re.match(regex, phone):
        return ""
    else:
        return "P"


def validate_date(date):
    """
    Validates the format of a date so that it is MM/DD/YYYY and must be a number between 1-12 MM and 1-31 DD.
    :param date: The date to be tested.
    :return: An empty string if date is valid, otherwise return D in invalid.csv.
    """
    regex = r'^(0[1-9]|1[0-2])/(0[1-9]|1\d|2\d|3[01])/\d{4}$'          # checks for MM/DD/YYYY format
    if re.match(regex, date):                                          # updated to accept 1-12 months and 0-31 days
        return ""
    else:
        return "D"


def validate_time(time):
    """
    Validates the format of a time so that it follows military time (HH:MM) and uses 00-23 HH and 00-59 MM.
    :param time: The time to be tested.
    :return: An empty string if time is valid, otherwise return T in invalid.csv.
    """
    regex = r'^([1]\d|2[0-3]):([0-5]\d)$'       # HH:MM military only allows 00-23 hours and 00-59 minutes to be valid
    if re.match(regex, time):
        return ""
    else:
        return "T"


def process_file():
    """
    Process the input CSV file to validate data and write valid and invalid records to separate CSV files.
    Note: The input CSV file must be separated by pipe delimiters '|'

    This function reads the data from 'input.csv' and validates each record. Valid records are written
    to 'valid.csv', while invalid records are written to 'invalid.csv'. Each invalid record includes an error code
    indicating the nature of the validation error(s).

    If a record passes all validation checks, it is written to 'valid.csv' with fields separated by commas.
    If a record fails one or more validation checks, it is written to 'invalid.csv' with fields separated by pipes '|',
    and an error code indicating the type of validation error(s) can be found on the left side of the record.
    :return: None
    """
    with open("input.csv", newline='') as input_file, \
         open("valid.csv", 'w', newline='') as valid_file, \
         open("invalid.csv", 'w', newline='') as invalid_file:
        input_reader = csv.reader(input_file, delimiter='|')
        valid_writer = csv.writer(valid_file, delimiter=',')
        invalid_writer = csv.writer(invalid_file, delimiter='|')

        for line in input_reader:
            error_string = ""
            if len(line) != 6:
                # If input doesnt have all 6 data types, send it to invalid with an error type 'C' without other
                # validations
                error_string = "C"
            else:
                error_string += validate_id(line[0])        # Call the validate_id function
                error_string += validate_name(line[1])      # Call the validate_name function
                error_string += validate_email(line[2])     # Call the validate_email function
                error_string += validate_phone(line[3])     # Call the validate_phone function
                error_string += validate_date(line[4])      # Call the validate_date function
                error_string += validate_time(line[5])      # Call the validate_time function

            if error_string == "":
                if len(line) > 1:
                    # If there are no errors found in the input, write it to valid.csv
                    names = line[1].split(',')      # Separates names with comma and eventually strips spaces
                    valid_writer.writerow([
                        line[0], names[1].strip(), names[0].strip(),
                        line[2], line[3], line[4], line[5]
                    ])
            else:
                # Adds the error type to the beginning of the record and writes the invalid record to invalid.csv
                line.insert(0, error_string)
                invalid_writer.writerow(line)


if __name__ == '__main__':
    process_file()

