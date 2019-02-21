"""
问题60：n个骰子的点数
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。
"""


def dices_probability(n):
    """
    :param n:number of dices
    :return: dict of possible value
    """
    times = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
    for i in range(2,n+1):
        cache = {}
        for val in range(1 * i, 6 * i + 1):
            cache[val] = 0
            j = 1
            while j <= 6:
                if (val - j) in times:
                    cache[val] += times[val - j]
                j += 1
        times = cache

    for val in times:
        from fractions import Fraction
        times[val] = Fraction(times[val], 6 ** n)
        # times[val] = times[val] / 6 ** n
    return times

print(dices_probability(11))