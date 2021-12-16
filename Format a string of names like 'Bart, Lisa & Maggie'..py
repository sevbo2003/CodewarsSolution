"""https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python"""


def namelist(names):
    if len(names) == 0:
        return ''
    names = [i['name'] for i in names]
    for i in names:
        if len(names) == 1:
            return names[0]
        else:
            return ', '.join(names[:-1]) + f' & {names[-1]}'


names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]
# returns 'Bart, Lisa & Maggie'
print(namelist(names))
# --> 🙂
