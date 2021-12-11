"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python"""

from functools import reduce


def parts_sums(ls):
    if len(ls) == 0:
        return [0]
    else:
        totalSum = reduce(lambda a, b: a + b, ls)
        sumList = [totalSum]
        for i in range(1, len(ls) + 1):
            totalSum -= ls[i - 1]
            sumList.append(totalSum)
        return sumList


print(parts_sums([0, 1, 3, 6, 10]))

# --> Easy peasy 😁 😎 😉 🤞 ✌  (☞ﾟヮﾟ)☞