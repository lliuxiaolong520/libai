"""
李白喝酒，起始有2斗酒，遇到酒店酒翻倍，遇到花店喝一斗。
5个酒店10个花店后刚好喝完。问李白有多少种可能？
"""
import itertools


def info(list1):
    n = 2
    for i1 in list1:
        if i1 == 2:
            n *= 2
        else:
            n -= 1
            
    if n == 1:
        return True


s = [1, 2]

a = itertools.product(s, s, s, s, s, s, s, s, s, s, s, s, s, s)

b = 0
for i in a:
    if sum(i) == 20:
        a3 = info(i)
        if a3:
            b += 1

print(b)
