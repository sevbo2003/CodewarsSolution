"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python"""


def scramble(s1, s2):
    ans = [i for i in s2 if i in s1]
    return len(ans) == len(s2)


print(scramble('rkqodlw', 'world'))

# --> 👌✔✔✔
