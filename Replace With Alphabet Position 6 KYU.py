"""https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python"""

from string import ascii_lowercase
def alphabet_position(text):
    return ' '.join([str(ascii_lowercase.index(i)+1) for i in text.lower() if i.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))

# --> ✔ 😜
