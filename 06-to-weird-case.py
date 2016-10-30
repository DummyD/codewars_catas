# https://www.codewars.com/kata/weird-string-case/python


def to_weird_case(string):
    return ' '.join(''.join(x[i].upper() if i % 2 is False else x[i] for i in range(len(x))) for x in string.split())
