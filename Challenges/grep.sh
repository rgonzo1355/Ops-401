#!/bin/bash

# If you want to do it in python
: '
# Open the input file for reading
with open('testfile.txt', 'r') as file:
    # Open output files for each severity level
    with open('warning.txt', 'w') as warning_file, \
         open('error.txt', 'w') as error_file, \
         open('threat.txt', 'w') as threat_file:
        
        for line in file:
            # Check if the line contains "WARNING," "ERROR," or "THREAT"
            if 'WARNING' in line:
                warning_file.write(line)
            elif 'ERROR' in line:
                error_file.write(line)
            elif 'THREAT' in line:
                threat_file.write(line)
'

# Extract lines containing "WARNING" and write to warning.txt
grep "WARNING" testfile.txt > warning.txt

# Extract lines containing "ERROR" and write to error.txt
grep "ERROR" testfile.txt > error.txt

# Extract lines containing "THREAT" and write to threat.txt
grep "THREAT" testfile.txt > threat.txt

