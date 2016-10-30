# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/python


def digital_root(n):
    return n if n < 10 else digital_root(sum(int(i) for i in str(n)))
