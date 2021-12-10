"""https://www.codewars.com/kata/514b92a657cdc65150000006/train/python"""


def solution(number):
    nums = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0 and i % 15 != 0:
            nums.append(i)
        elif i % 15 == 0:
            nums.append(i)
    return sum(nums)


# -->  ✔