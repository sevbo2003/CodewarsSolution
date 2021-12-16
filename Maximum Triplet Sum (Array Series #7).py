"""https://www.codewars.com/kata/5aa1bcda373c2eb596000112/train/python"""


def max_tri_sum(numbers):
    lst = []
    for i in sorted(numbers,reverse=True):
        if i not in lst:
            lst.append(i)
        if len(lst) == 3:
            break
    return sum(lst)
numbers = [2,1,8,0,6,4,8,6,2,4]
print(max_tri_sum(numbers))  # --> 18
# --> ಠ_ಠ
