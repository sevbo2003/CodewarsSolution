"""https://www.codewars.com/kata/58afce23b0e8046a960000eb/train/python"""


def withdraw(amount):
    result = [0, 0, 0]
    remainder = amount % 100
    if (remainder == 10 or remainder == 30) and (amount >= 100):
        result[0] = int(amount / 100) - 1
    else:
        result[0] = int(amount / 100)
    amount -= result[0] * 100

    if (amount % 20 == 0):
        result[1] = 0
    elif (amount < 50):
        result[1] = 0
    else:
        result[1] = 1
    amount -= result[1] * 50

    result[2] = int(amount / 20)
    return (result)


print(withdraw(260))