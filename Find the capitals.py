"""https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python"""

def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]


print(capitals('CodEWaRs'))