# https://www.codewars.com/kata/counting-duplicates/python


from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())
    return len([x for x in counter if counter[x] > 1])
