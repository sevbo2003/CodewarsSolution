def next_bigger(n):
    digits = [int(i) for i in str(n)]
    maks = int(''.join(sorted([i for i in str(n)], reverse=True)))
    if n >= int(''.join(sorted(str(n), reverse=True))):
        return -1
    else:
        for i in range(n + 1, maks + 1):
            if sorted(str(i)) == sorted(str(n)):
                return i


print(next_bigger(144))
# 😎 Easypeasy
