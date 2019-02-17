"""
面试题57：和为s的数字
题目1：和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

例：
输入：[1, 2, 4, 7, 11, 15]
输出：4, 11
"""


def two_numbers_with_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            break
    return numbers[left], numbers[right]