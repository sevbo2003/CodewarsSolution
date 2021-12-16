"""https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python"""


def find_outlier(integers):
    odds = [i for i in integers if i % 2 != 0]
    evens = [i for i in integers if i % 2 == 0]
    return odds[0] if len(odds) == 1 else evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))

# --> 😍 😎
