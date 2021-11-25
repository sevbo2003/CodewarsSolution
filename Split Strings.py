# 6KYU
"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
"""


def solution(s):
    new = []
    for i in range(0, len(s), 2):
        string = ''
        try:
            string+=s[i]+s[i+1]
        except:
            string+=s[i]+'_'
        new.append(string)
    return new


print(solution("asdfads"))