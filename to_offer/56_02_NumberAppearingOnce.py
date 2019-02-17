"""
面试题56:数组中数字出现的次数
题目2：数组中唯一只出现一次的数字
再一个数组中除一个数字只出现一次之外，其他数字都出现了三次。
"""


def number_appearing_once(nums):
    cache = [0] * 32
    for num in nums:
        bit_mask = 1
        for i in range(31,-1,-1):
            if num & bit_mask:
                cache[i] += 1
            bit_mask  = bit_mask << 1
    ans = 0
    for i in range(32):
        ans = ans << 1
        ans += cache[i] % 3
    return ans if ans < 2 ** 31 else ans - 2 ** 32

def number_appearing_once_2(nums):
    a, b = 0, 0
    for num in nums:
        b = ~a & (b ^ num)
        a = ~b & (a ^ num)
    return b

nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print(number_appearing_once(nums))