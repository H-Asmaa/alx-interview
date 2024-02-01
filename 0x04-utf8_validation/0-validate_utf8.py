#!/usr/bin/python3
"""
0x04-utf8_validation
"""


def validUTF8(data):
    """A method that determines if a given data set
    represents a valid UTF-8 encoding."""
    try:
        data = bytes(i & 0xFF for i in data)
        data.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False
