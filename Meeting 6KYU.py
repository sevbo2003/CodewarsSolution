"""https://www.codewars.com/kata/59df2f8f08c6cec835000012/train/python"""


def meeting(s):
    new = []
    for i in s.split(';'):
        i = i.split(':')
        text = f"({i[1]}, {i[0]})"
        new.append(text.upper())
    new = sorted(new)
    return ''.join(new)


s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
# --> "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

print(meeting(s))

# --> !Not easy but not difficult too 🤗
