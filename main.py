#!/user.bin.env python3

"""
This data validator will read input.csv and validate valid data and send it to valid.csv and send any invalid data to
invalid.csv.

The data validator will check for:
    -Invalid id that isn't an integer
    -Invalid names that are not in a "last name, first name" format
    -Invalid email that are not in proper email format or not .edu extension
    -Invalid phone numbers that are not in a 111-222-3333 format
    -Invalid date that are not in a MM/DD/YYYY format
    -Invalid time that are not in a HH:MM military format
"""

__author__ = 'Jonathan Nissen'
__version__ = '1.0'
__date__ = '4/16/2024'
__status__ = 'Development'


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Jonathan Nissen')

