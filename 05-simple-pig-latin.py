# https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_it(text):
    return ' '.join(x[1:] + x[0] + 'ay' if x.isalpha() else x for x in text.split())
