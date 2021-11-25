# 7KYU
"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
"""


def find_short(s):
    return min([len(word) for word in s.split()])



s = "bitcoin take over the world maybe who knows perhaps"
print(find_short(s))