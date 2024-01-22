#!/usr/bin/python3
#by riksvic
def safe_print_integer(value):
    """This prints an integer with
    "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError or ValueError is
        encounted - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
