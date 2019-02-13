"""
面试题53：在排序数组中查找数字
题目2：0~n-1中缺失的数字。
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""

def missing_num(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == mid:
            left = mid + 1
        else:
            if nums[mid - 1] == mid - 1:
                return mid
            right = mid - 1
    return left

print(missing_num([]))