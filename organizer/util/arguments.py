import sys


def is_option(option: str) -> bool:
    return ("--" + option) in sys.argv
