"""https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python"""


def is_prime(num):
    if num > 1:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True
    else:
        return False


print(is_prime(73284098))


# --> A bit difficult ^_^
# P.s I love PEP 8 standart 💖
