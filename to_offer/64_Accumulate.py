"""
面试题64：求1+2+…+n
题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、
case等关键字及条件判断语句（A?B:C）。
"""


def accumulate(n):
    return n and accumulate(n-1) + n

def accumulate_2(n):
    choice = {0:0}
    return n + choice.get(n-1, accumulate(n-1))


print(accumulate_2(10))