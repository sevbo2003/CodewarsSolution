"""https://www.codewars.com/kata/537529f42993de0e0b00181f/train/python"""


def count_inversions(array):
    cont = 0
    for num, item in enumerate(array):
        for j in array[num+1:]:
            if item > j:
                cont += 1
    return cont


array = [4, 3, 2, 1]
print(count_inversions(array))
# --> 😎 😛
