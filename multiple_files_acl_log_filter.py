#!/usr/bin/env python3

# This script searches a log file for lines containing a specific ACL event string
# and prints those lines. It also measures the time taken to complete the search.

import re  # For regular expression search
import datetime  # For timing the script execution

# Record the start time
startTime = datetime.datetime.now()

# Open the log file in read mode
with open('sample_log_anonymized.log', 'r') as f:
    # Iterate over each line in the file
    for line in f.readlines():
        # Check if the line contains the specified ACL log pattern
        if re.search('ACLLOG-5-ACLLOG_FLOW_INTERVAL', line):
            print(line)  # Print matching line to the console

# Record the end time
endTime = datetime.datetime.now()

# Calculate and print the elapsed time
elapsedTime = endTime - startTime
print("Time Elapsed: " + str(elapsedTime))
