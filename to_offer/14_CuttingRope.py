"""
面试题：剪绳子
题目：给你一段长度为n的绳子，请把绳子剪成m段（m、n都是整数， n > 1并且m > 1），
每段绳子的长度记为k[0], k[1]...k[m]。请问k[0] x k[1] x ... x k[m]可能的最大乘
积是多少？
例：
n = 8 m = 3
最大乘积 = 2 * 3 * 3 = 18
"""

def cutting_rope(l_rope):
    """
    :param l_rope: length of rope
    :return: max of mul
    """
    if l_rope < 2:
        return 'Invalid Input'
    max_mul = [0, 1, 2, 3] + [0]*(l_rope-3)
    for l in range(4, l_rope+1):
        max_mul[l] = max(max_mul[res] * max_mul[l-res] for res in range(1, l-1))
    return max_mul[l_rope]

def cutting_rope_greed(l_rope):
    """
    greed algorithm
    :param l_rope: length of rope
    :return: max of mul
    """
    if l_rope < 2:
        return 'Invalid Input'
    # ans = 1
    # while l_rope >= 5:
    #     ans *= 3
    #     l_rope -= 3
    # ans *= l_rope
    # return ans
    ans = pow(3, l_rope // 3)
    if l_rope % 3 == 1:
        ans = ans // 3 * 4
    elif l_rope % 3 == 2:
        ans *= 2
    return ans

print(cutting_rope_greed(7))