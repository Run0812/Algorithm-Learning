"""
面试题21：调整数组顺序使奇数位于偶数前面
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于
数组的前半部分，所有偶数位于数组的后半部分。
"""

def reorder_array(nums, key):
    """
    :param nums:array
    :param key: criterion function True in front False at back
    :return: ordered array
    """
    head = 0
    end = len(nums) - 1
    while head < end:
        if key(nums[head]):
            head += 1
        else:
            if key(nums[end]):
                nums[head], nums[end] = nums[end], nums[head]
                head += 1
                end -= 1
            else:
                end -= 1
    return nums


def is_odd(n):
    return n % 2

nums = [1,3,4,65,7,12,4,6,8,11]
reorder_array(nums, is_odd)
print(nums)