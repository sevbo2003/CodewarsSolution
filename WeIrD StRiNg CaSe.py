"""https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python"""


def to_weird_case(string):
    string = string.split()
    final = []
    for word in string:
        word = [i for i in word]
        for i in range(len(word)):
            if i % 2 == 0:
                word[i] = word[i].upper()
        final.append(''.join(word))
    return ' '.join(final)


print(to_weird_case('test'))  # => returns 'WeIrD StRiNg CaSe'

# --> 😘✔✔✔✔✔✔👌😍