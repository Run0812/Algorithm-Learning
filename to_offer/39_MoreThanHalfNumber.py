"""
面试题39：数组中出现次数超过一半的数字
题目：数组种有一个数字出现的次数超过数组长度的一半，请找出这个数字。

例：
输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
"""

def more_than_half_number(nums):
    """
    :param nums:list
    :return: mode
    """
    count = 0
    most = nums[0]
    for n in nums:
        if n == most:
            count += 1
        else:
            count -= 1
        if count < 0:
            most = n
            count = 1
    return most

more_than_half_number([2,2,1,1,1,2,2])