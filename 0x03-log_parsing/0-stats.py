#!/usr/bin/python3

import sys

def print_metrics(status_codes, total_size):
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except Exception:
        return None, None, None

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_metrics(status_codes, total_size)
        
        ip_address, status_code, file_size = parse_line(line)
        
        if ip_address is not None and status_code in status_codes:
            total_size += file_size
            status_codes[status_code] += 1
        
        line_count += 1
    
    print_metrics(status_codes, total_size)

except KeyboardInterrupt:
    print_metrics(status_codes, total_size)
    raise

