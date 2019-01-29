"""
面试题46：把数字翻译成字符串
题目：给定一个数字，我们按照如下规则把它翻译位字符串：
0 = 'a'; 1 = 'b';...; 25 = 'z'，一个数字可能有多种翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

例：
12258，有5种翻译："bccfi", "bwfi", "bczi", "mcfi", "mzi"。
"""

def trans_nums_to_strs(nums):
    """
    :param nums: number
    :return: number of translations
    """
    nums = str(nums)
    cache = [1, 1]
    for i in range(1, len(nums)):
        if 9 < int(nums[i-1:i+1]) < 26:
            cache[1], cache[0] = cache[0] + cache[1], cache[1]
        else:
            cache[0] = cache[1]
    return cache[1]

print(trans_nums_to_strs(12258))