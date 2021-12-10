"""https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb/train/python"""


def find_missing_numbers(arr):
    if len(arr) in [1]:
        return []
    else:
        nums = []
        for i in range(min(arr), max(arr)):
            if i not in arr:
                nums.append(i)
        return nums


print(find_missing_numbers([-3,-2,1,4]))