"""
面试题9：用两个栈实现队列
题目：用两个栈实现一个队列。具备在尾部插入节点，在头部弹出节点的功能。
例：
[1,2,3,4]
增加5，[1,2,3,4,5]
弹出，[2,3,4,5] return 1
"""

class Stack(object):

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
        return

    def pop(self):
        return self.data.pop(0) if self.data else None

    def __bool__(self):
        """
        :return: if empty
        """
        return True if self.data else False


class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        self.stack1.push(x)
        return

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def __str__(self):
        """
        :return: print Queue head -> end
        """
        return str(self.stack2.data + self.stack1.data)

q = Queue()
data = [1,2,3,4,5]
for n in data:
    q.push(n)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
q.push(0)
print(q)
print(q.pop())
q.push(6)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
