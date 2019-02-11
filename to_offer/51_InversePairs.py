"""
面试题51：数组中的逆序对
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个
逆序对。输入一个数组，求出这个数组中的逆序对的总数。

例：
在数组中{7, 5, 6, 4}中，一共存在5个逆序对，分别是(7, 6)、(7, 5)、(7, 4)、
(6, 4)、(5, 4)
"""

def inverse_pairs(array):

    def merge_sort(array):

        def merge(left, right):
            nonlocal inverse
            sorted = []
            i, j = len(left) - 1, len(right) - 1
            while i >= 0 and j >= 0:
                if left[i] <= right[j]:
                    sorted =  [right[j]] + sorted
                    j -= 1
                else:
                    sorted = [left[i]] + sorted
                    inverse += j+1
                    i -= 1
            sorted = left[:i+1] + sorted
            sorted = right[:j+1] + sorted
            return sorted

        length = len(array)
        mid = length // 2
        if length <= 1:
            return array
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)

    inverse = 0
    merge_sort(array)

    return inverse

print(inverse_pairs([0]))
