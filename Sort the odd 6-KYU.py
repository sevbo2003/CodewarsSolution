"""https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python"""


def sort_array(source_array):
    odds = sorted([i for ind, i in enumerate(source_array) if i % 2 == 1])
    # print(odds)
    x = 0
    for pos, num in enumerate(source_array.copy()):
        if num % 2 == 1:
            source_array[pos] = odds[x]
            x += 1
    return source_array


source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
print(sort_array(source_array))
# 😁 😎 😀 😉 🥰
