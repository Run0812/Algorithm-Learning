"""
面试题63：股票的最大利润
题目：假设把把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股
票可能获得的利润是多少？

例：
一只股票在某些时间节点的价格为{9, 11, 8, 5, 7, 12, 16, 14}。
如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
"""


def maximal_profit(prices):
    """
    :param prices:prices list
    :return: max profit
    """
    max_p = c_p = 0
    for i in range(1, len(prices)):
        c_p += prices[i] - prices[i - 1]
        if c_p < 0:
            c_p = 0
        if c_p > max_p:
            max_p = c_p
    return max_p
