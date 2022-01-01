"""https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python"""


def number_of_pairs(gloves):
    x = list(set(gloves))
    a = 0
    for i in x:
        if gloves.count(i) > 1:
            a += gloves.count(i) // 2
    return a

# A bit difficult 😎
