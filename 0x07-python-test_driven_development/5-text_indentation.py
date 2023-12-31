#!/usr/bin/python3
""" text_indentation
Returns "text" in the specified format:
2 newlines after each ['.', '?', ':']
"""


def text_indentation(text):
    """ prints "text" with 2 newlines after each of these char: ['.', '?', ':']
    checks if "text" is a str
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    toCatAfter = ['.', '?', ':']

    # Removes the space after special chars
    idx = 0
    for items in text:
        if items in toCatAfter:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    # Cats '\n\n' after the special char with removed space
    idx = 0
    for items in text:
        if items in toCatAfter:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
