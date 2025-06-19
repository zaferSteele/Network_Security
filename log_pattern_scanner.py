#!/usr/bin/env python3

import re
import datetime

# Record the start time to measure script execution duration
startTime = datetime.datetime.now()

# Compile regular expressions for matching specific log patterns
# Pattern 1: Matches firewall ACL flow interval logs
term1 = re.compile('ACLLOG-5-ACLLOG_FLOW_INTERVAL')
# Pattern 2: Matches PAM authentication failures (e.g., failed logins)
term2 = re.compile('PAM: Authentication failure')

# List of log files to process
fileList = ['sample_log_anonymized.log', 'sample_log_anonymized_1.log']

# Iterate through each log file
for log in fileList:
    with open(log, 'r') as f:
        # Read each line and search for matches with either pattern
        for line in f.readlines():
            if re.search(term1, line) or re.search(term2, line):
                print(line)

# Record the end time
endTime = datetime.datetime.now()
# Calculate and print the elapsed time
elapsedTime = endTime - startTime
print("Time Elapsed: " + str(elapsedTime))
