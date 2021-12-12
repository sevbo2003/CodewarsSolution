"""https://www.codewars.com/kata/59ec2d112332430ce9000005/train/python"""


def solve(a, b):
    factors = [i for i in range(2, b+1) if b % i == 0]
    for c in factors:
        if a % c == 0:
            return True
    return False


print(solve(15, 12))
