#!/usr/bin/python3
import sys
import signal


def sig_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(stats_codes.keys()):
        print("{}: {}".format(code, stats_codes[code]))


total_size = 0
stats_codes = {}
line_count = 0

signal.signal(signal.SIGINT, sig_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        size = int(parts[-1])
        stats_code = int(parts[-2])
        total_size += size
        if stats_code in stats_codes:
            stats_codes[stats_code] += 1
        else:
            stats_codes[stats_code] = 1
    except Exception:
        pass

    line_count += 1
    if line_count % 10 == 0:
        print_stats()

print_stats()
