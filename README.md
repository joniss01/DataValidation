# Data Validation 

This Python script validates data in a CSV file and separates valid records into one file and invalid records into another file based on predefined criteria.

## Features
- Validates data elements including ID, name, email, phone number, date, and time.
- Outputs valid records to a CSV file (valid.csv).
- Outputs invalid records along with error codes to a CSV file (invalid.csv).
- Provides detailed error reports for invalid data types.
- The data validator will check for:
    - C = Invalid data element count
    - I = Invalid id that isn't an integer
    - N = Invalid names that are not in a "last name, first name" format
    - E = Invalid email that are not in proper email format or not .edu extension
    - P = Invalid phone numbers that are not in a 111-222-3333 format
    - D = Invalid date that are not in a MM/DD/YYYY format
    - T = Invalid time that are not in a HH:MM military format

## What I learned
This project taught me how to utilize regular expressions (regex) in Python for data validation. Regex allowed me to define patterns for validating various data formats, such as email addresses, phone numbers, dates, and times. This skill may be useful for future projects involving data processing and validation.
