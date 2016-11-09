# https://www.codewars.com/kata/5547cc7dcad755e480000004


def removNb(n):
    result = []
    s = n * (n + 1) / 2

    for i in range(1, n + 1):
        c = (s - i) / (i + 1)
        if n >= c == int(c):
            result.append((i, c))
    return result
