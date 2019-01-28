"""
面试题44：数字序列中某一位的数字
题目：数字以0123456789101112131415...的格式序列化到一个字符序列中。
在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
"""

def digits_in_sequence(n):
    if n < 10:
        return n
    else:
        n -= 10
        num = 90
        digits = 2
        nums = num * digits
    while n > nums:
        n -= nums
        num *= 10
        digits += 1
        nums = num * digits
    else:
        res_digit = str(10 ** (digits - 1) + (n // digits))[n % digits]
    return int(res_digit)

print(digits_in_sequence(1001))