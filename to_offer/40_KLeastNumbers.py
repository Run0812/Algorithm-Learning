"""
面试题40：最小的K个数
题目：输入n个整数，找出其中的最小的k个数。

例：
输入[4, 5, 1, 6, 2, 7, 3, 8] K = 4
输出[1, 2, 3, 4]
"""

def k_least_nums(nums, k):
    """
    :param nums:list
    :param k: the least boundary
    :return: k least nums list
    """

    def partition(nums, left, right, k):
        """
        :param nums: num list
        :param left: partition left boundary
        :param right: partition right boundary
        :param k: the least boundary
        :return:k least nums list
        """
        pos = left
        for i in range(left,right):
            if nums[i] <= nums[right]:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        nums[pos], nums[right] = nums[right], nums[pos]
        if pos == k - 1:
            return nums[:k]
        elif pos < k - 1:
            return partition(nums, pos+1, right, k)
        elif pos > k - 1:
            return partition(nums, left, pos-1, k)
    if not nums:
        return []
    return partition(nums, 0, len(nums) - 1, k)

def k_least_nums_heap(nums, k):
    from datstru import Heap
    big_heap = Heap()
    for n in nums:
        if len(big_heap) < k:
            big_heap.insert(n)
        else:
            if n < big_heap.top():
                big_heap.pop()
                big_heap.insert(n)
    return big_heap.data[1:]

nums = [4, 5, 1, 6, 2, 7, 3, 8, 0,-1]
print(k_least_nums_heap(nums, 4))
from datstru import  Heap
h = Heap([6,7,8])
h.extend([1,2,3,4,5])
print()