"""
面试题16：数值的整数次方
题目：实现函数double Power(double base, int exponent), 求base的exponent次方，
不得使用库函数。同时不需要考虑大数问题。
"""

def power(base, exponent):
    """
    :param base: a
    :param exponent: b
    :return: a^b
    """
    flag = 1
    if base == 0:
        return 0
    if exponent < 0 :
        flag = 0
        exponent = - exponent
    def binary_pow(base, exponent):
        if exponent == 1:
            return base
        if exponent == 0:
            return 1
        res = binary_pow(base, exponent >> 1)
        res *= res
        if exponent & 1:
            res *= base
        return res
    res = binary_pow(base, exponent)
    return res if flag else 1 / res

print(power(2,-1))