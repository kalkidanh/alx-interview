#!/usr/bin/python3
""" UTF-8 validation."""


def validUTF8(data):
    """ Method that validates a dataset for UTF-8 encoding."""
    num_bytes = 0
    fil1 = 1 << 7
    fil2 = 1 << 6

    for num in data:
        fil = 1 << 7
        if num_bytes == 0:
            while fil & num:
                num_bytes += 1
                fil = fil >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & fil1 and not (num & fil2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
