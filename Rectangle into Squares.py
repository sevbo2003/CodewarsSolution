"""https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python"""


def sqInRect(x, y):
    if x == y:
        return None

    result = []
    while y != x:
        if y > x:
            y -= x
            result.append(x)
        elif x > y:
            x -= y
            result.append(y)

    result.append(y)

    return result

print(sqInRect(5, 3))
# --> Thanks to </harmo> for helping me 😁
