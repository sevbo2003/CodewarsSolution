"""https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python"""


def camel_case(string):
    return ''.join([i.capitalize() for i in string.split()])


print(camel_case("camel case word"))

# --> ✌ 😎 ✔
