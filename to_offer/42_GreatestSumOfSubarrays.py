"""
面试题42：连续子数组的最大和
题目：输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数
组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度：O(n)

例：
输入：[1, -2, 3, 10, -4, 7, 2, -5]
输出：18, [3, 10, -4, 7, 2]
"""

def greatest_sum_of_subarrays(nums):
    """
    :param nums: array
    :return: max sum of subarray
    """
    max = sub_sum = float('-inf')
    for n in nums:
        if sub_sum + n <= n:
            sub_sum = n
        else:
            sub_sum += n
        if sub_sum > max:
            max = sub_sum
    return max

print(greatest_sum_of_subarrays([1, -2, 3, 10, -4, 7, 2, -5]))