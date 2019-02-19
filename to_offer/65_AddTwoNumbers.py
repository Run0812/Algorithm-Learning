"""
面试题65：不用加减乘除做加法
题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷
四则运算符号。
"""


def add(a, b):
    while b:
        a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        # limit the bit length < 32
    return a if a < 0X7fffffff else ~(a ^ 0xFFFFFFFF)

s = add(-1,1)
