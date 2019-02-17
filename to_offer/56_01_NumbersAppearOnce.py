"""
面试题56:数组中数字出现的次数
题目1：数组中只出现一次的两个数字
一个整型数组中除了两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度O(n)，空间复杂度O(1)。

例：
输入：[2, 4, 3, 6, 3, 2, 5, 5]
输出：4, 6
"""


def numbers_appear_once(nums):
    if not nums:
        return None
    s = n1 = n2 = 0
    for num in nums:
        s ^= num
    bit = 0
    while s & 1 == 0:
        s = s >> 1
        bit += 1
    div = 1 << bit
    for num in nums:
        if num & div:
            n1 ^= num
        else:
            n2 ^= num
    return n1, n2

print(numbers_appear_once([]))