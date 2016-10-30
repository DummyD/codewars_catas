# https://www.codewars.com/kata/the-observed-pin/python


from itertools import product


PIN = {'1': ('1', '2', '4'),
       '2': ('1', '2', '3', '5'),
       '3': ('2', '3', '6'),
       '4': ('1', '4', '5', '7'),
       '5': ('2', '4', '5', '6', '8'),
       '6': ('5', '6', '9', '3'),
       '7': ('4', '7', '8'),
       '8': ('7', '5', '8', '9', '0'),
       '9': ('6', '8', '9'), '0': ('0', '8')}


def get_pins(observed):
    return [''.join(a) for a in product(*(PIN[b] for b in observed))]
