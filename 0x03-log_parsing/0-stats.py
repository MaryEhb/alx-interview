#!/usr/bin/python3
'''0. Log parsing'''
import sys
import re
import random


regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (200|301|400|401|403|404|405|500) (\d{1,4})'  # nopep8

if __name__ == '__main__':
    i = 0
    tot_file_size = 0
    output = []
    try:
        for line in sys.stdin:
            if (i % 10 == 0 and i != 0) or i > 10:
                print('File size: {}'.format(tot_file_size))
                output_sorted = sorted(output, key=lambda x: x['status'])
                for x in output_sorted:
                    print('{}: {}'.format(x['status'], x['num']))
                i = 0

            match = re.match(regex, line.rstrip())
            if match:
                file_size = int(match.group(3))
                status_code = int(match.group(2))

                found = False
                for x in output:
                    if x['status'] == status_code:
                        x['num'] += 1
                        found = True
                if not found:
                    output.append({'status': status_code, 'num': 1})

                tot_file_size += file_size
            i += 1
    finally:
        print('File size: {}'.format(tot_file_size))
        output_sorted = sorted(output, key=lambda x: x['status'])
        for x in output_sorted:
            print('{}: {}'.format(x['status'], x['num']))
