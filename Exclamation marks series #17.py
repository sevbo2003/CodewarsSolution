"""https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python"""


def balance(left, right):
    marks = {'!': 2, '?': 3}
    ball = 0
    for a in left:
        ball += marks[a]
    for b in right:
        ball -= marks[b]
    if ball<0:
        return 'Right'
    elif ball>0:
        return 'Left'
    else:
        return 'Balance'


print(balance("!!???!????", "??!!?!!!!!!!"))
# --> Easy
