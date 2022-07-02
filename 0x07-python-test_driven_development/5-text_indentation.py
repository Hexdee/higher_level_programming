#!/usr/bin/python3
"""Module text_indentation"""


def text_indentation(text):
    """Text_indentation.

    Args:
        text: Text to transform.

    Returns:
        Text transformed.

    """
    if type(text) != str:
        raise TypeError('text must be a string')

    for i in ['.', '?', ':']:
        text = (i + '\n\n').join([row.strip(' ') for row in text.split(i)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
