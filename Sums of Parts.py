"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python"""

def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result


print(parts_sums([0, 1, 3, 6, 10]))

# --> Easy peasy 😁 😎 😉 🤞 ✌  (☞ﾟヮﾟ)☞