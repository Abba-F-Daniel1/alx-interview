#!/usr/bin/python3
"""
This module reads from stdin, computes metrics,
and handles keyboard interruptions.
It calculates the total file size and
counts the number of occurrences of each status code.
"""

import sys
import signal
import re
from collections import defaultdict


def signal_handler(sig, frame):
    """
    Handles the SIGINT signal by printing the statistics
    and exiting the program.
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """
    Prints the total file size and
    the number of occurrences of each status code.
    The status codes are printed in ascending order.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


total_size = 0
status_codes = defaultdict(int)
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

pattern = (r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
           r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

for line in sys.stdin:
    """
    For each line in stdin, it checks if the line matches the pattern.
    If it does, it increments the count for the status code
    and adds the file size to the total size.
    After every 10 lines, it prints the statistics.
    """
    match = re.search(pattern, line)
    if match:
        status_code = match.group(3)
        file_size = match.group(4)
        status_codes[status_code] += 1
        total_size += int(file_size)
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

print_stats()
