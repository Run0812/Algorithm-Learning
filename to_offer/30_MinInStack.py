"""
面试题30：包含min函数的栈
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
在该栈中，调用min、push及pop的时间复杂度都是O(1)。
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.        """

        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.data:
            min = x if self.data[-1][1] >= x else self.data[-1][1]
        else:
            min = x
        self.data.append((x, min))
        return

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]