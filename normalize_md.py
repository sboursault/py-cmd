# !/usr/bin/env python3

import re


def normalize(path: str):
    # Read in the file
    with open(path, 'r') as file:
        content = file.read()

    newContent = normalize_string(content)

    # Write the file out again
    with open(path, 'w') as file:
        file.write(newContent)


def normalize_string(content, max_line_length=120):
    content = remove_cr(content)
    result = ''
    for line in content.split('\n'):
        result += add_cr(line, max_line_length) + '\n'

    return result.rstrip('\n')


def add_cr(input: str, max_line_length=110):
    tmp = input
    result = ''

    while len(tmp) > 0:
        index = tmp.rfind(' ', 0, max_line_length)
        if index == -1 or len(tmp) < max_line_length:
            result += tmp
            tmp = ''
        else:
            result += tmp[0: index] + '\n'
            tmp = tmp[index + 1:]

    return result


def remove_cr(input):
    return re.sub(r"([^\n])( *\n)(\w)", r"\1 \3", input)


if __name__ == '__main__':
    normalize('Robert Iger - the ride of a lifetime.md')
