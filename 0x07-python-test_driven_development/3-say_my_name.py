#!/usr/bin/python3
"""Module say_my_name"""


def say_my_name(first_name, last_name=""):
    """say_my_name.

    Args:
        first_name: First name.
        second_name: Second name.

    Returns:
        My name is first_name second_name.

    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
