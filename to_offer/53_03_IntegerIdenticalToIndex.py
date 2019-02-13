"""
面试题53：在排序数组中查找数字
题目3：数组中数值和下标相等的元素。
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出
数组中任意一个数值等于其下表的元素。

例：
在数组{-3, -1, 1, 3, 5}中，数字3和它的下标相等。
"""

def integer_identical_to_index(nums):
    """
    :param nums: array
    :return: the number equals its index
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] < mid:
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
        else:
            break
    else:
        raise Exception('NO SUCH NUMBER')
    return mid

nums = [-1,1]
print(integer_identical_to_index(nums))