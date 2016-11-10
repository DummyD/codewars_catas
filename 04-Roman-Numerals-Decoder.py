SPQR = ((900, 'CM'), (1000, 'M'), (400, 'CD'), (500, 'D'), (90, 'XC'), (100, 'C'), (50, 'L'),
        (40, 'XL'), (9, 'IX'), (10, 'X'), (4, 'IV'), (5, 'V'), (1, 'I'))


def solution(roman, result=0, i=0):
    if roman == '':
        return result
    while SPQR[i][1] in roman:
        result += SPQR[i][0]
        roman = roman[len(SPQR[i][1]):]
    i += 1
    return solution(roman, result, i)
