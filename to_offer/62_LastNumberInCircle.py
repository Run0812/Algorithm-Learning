"""
面试题62：圆圈中最后剩下的数字l
题目：0, 1,..., n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除
第m个数字。求出这个圆圈剩下的最后一个数字。
"""


def last_number_in_circle(n, m):
    nums = list(range(n))
    count = 1
    i = 0
    while len(nums) > 1:
        if count == m:
            nums.pop(i)
            count = 1
            i -= 1
        else:
            count += 1
        i = i + 1 if i < len(nums) - 1 else 0
    return nums[0]

def last_number_in_circle_2(n, m):
    if n < 1 or m < 1:
        return -1

    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i

    return last

print(last_number_in_circle_2(5,3))