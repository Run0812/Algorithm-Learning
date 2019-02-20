"""
面试题59：队列的最大值
题目2：队列的最大值
请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back和
pop_front的时间复杂度都是O(1)。
"""


class Queue(object):

    def __init__(self):
        self.data = []
        self.max_data = []

    def pop(self):
        """
        pop out the head element
        :return: head element
        """
        if not self.data:
            raise Exception('Empty Queue Cannot Pop')
        if self.data[0] == self.max_data[0]:
            self.max_data.pop(0)
        return self.data.pop(0)

    def push(self, x):
        """
        push in the back
        :param x: element
        :return: None
        """
        self.data.append(x)
        while self.max_data and self.max_data[-1] < x:
            self.max_data.pop()
        self.max_data.append(x)
        return

    def max(self):
        """
        get the maximum element
        :return: max element
        """
        return self.max_data[0]


q = Queue()
q.push(2)
print(q.max())
q.push(4)
print(q.max())
q.push(4)
print(q.max())
q.push(3)
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())
q.pop()
print(q.max())
q.pop()
q.pop()