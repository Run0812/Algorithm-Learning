"""
面试题66：构建乘积数组
题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其
中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
"""


def construct_array(nums):

    l = len(nums)
    ans = [1 for i in range(l)]
    p = q = 1
    for i in range(l):
        ans[i] *= q
        ans[-i - 1] *= p
        q *= nums[i]
        p *= nums[-i - 1]
    return