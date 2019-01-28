"""
面试题45：把数组排成最小的数
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

例：
输入数组{3, 32, 321}, 打印321323。
"""

from functools import cmp_to_key
def sort_array_for_min_number(nums):
    # def cmp(a, b):
    #     return -1 if a + b < b + a else 1
    nums = [str(i) for i in nums]
    # nums.sort(key = cmp_to_key(cmp))
    nums.sort(key = cmp_to_key(lambda a,b:-1 if a + b < b + a else 1))
    return ''.join(nums).lstrip('0') or '0'

print(sort_array_for_min_number([3,32,321,0]))