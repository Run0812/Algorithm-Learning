"""
面试题233:1~n整数中1出现的次数
题目：输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。

例：
输入12，1 ~ 12这些整数中包含1的数字有1、10、11和12，1一共出现了5次。
"""

def number_of_1(n):
    """
    :param n: max number
    :return: times that digit 1 appear
    """
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

def number_of_1_2(n):
    """
    :param n: max number
    :return: times that digit 1 appear
    """
    num = str(n)
    first_digit = int(num[0])
    length = len(num)
    if length == 1 and first_digit == 0:
        return 0
    if length == 1 and first_digit > 1:
        return 1
    if first_digit > 1:
        count_fisrt_digit = 10 ** (length-1)
    else:
        count_fisrt_digit = int(num[1:]) + 1
    count_other_digit = first_digit * (length - 1) * 10 ** (length - 2)
    count_rec_digit = number_of_1_2(int(num[1:]))
    count = count_fisrt_digit + count_other_digit + count_rec_digit
    return count


print(number_of_1_2(12))