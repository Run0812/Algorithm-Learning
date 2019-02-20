"""
面试题51：数组中的逆序对
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个
逆序对。输入一个数组，求出这个数组中的逆序对的总数。

例：
在数组中{7, 5, 6, 4}中，一共存在5个逆序对，分别是(7, 6)、(7, 5)、(7, 4)、
(6, 4)、(5, 4)
"""

def inverse_pairs(array):
    """
    :param array:array
    :return: number of inverse pairs
    """
    def merge_sort(nums, left, right):
        """
        :param nums:total array
        :param left: left index
        :param right: right index
        :return: sorted array
        """
        def merge(left, right):
            """
            :param left:left subarray
            :param right:right subarray
            :return:sorted array
            """
            nonlocal inverse
            i, j = len(left) - 1, len(right) - 1
            k = i + j + 1
            sorted = [0] * (k+1)
            while i >= 0 and j >= 0:
                if left[i] <= right[j]:
                    # sorted =  [right[j]] + sorted
                    sorted[k] = right[j]
                    j -= 1
                else:
                    # sorted = [left[i]] + sorted
                    sorted[k] = right[i]
                    inverse += j+1
                    i -= 1
                k -= 1
            # sorted = left[:i+1] + sorted
            # sorted = right[:j+1] + sorted
            sorted[:k+1] = left[:i+1] or right[:j+1]
            return sorted

        mid = (left + right) // 2
        if right - left <= 1:
            return nums[left:right]
        left = merge_sort(array, left, mid)
        right = merge_sort(array, mid, right)
        return merge(left, right)

    inverse = 0
    merge_sort(array, 0, len(array))

    return inverse

print(inverse_pairs([1,2,3,4,7,6,4,4]))
