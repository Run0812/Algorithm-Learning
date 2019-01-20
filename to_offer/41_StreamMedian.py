"""
面试题41：数据流中的中位数
题目：如何得到一个数据流中的中位数？如果数据流中读出奇数个值，那么中位数就是所有
数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值
排序后中间两个数的平均值。
"""

def stream_median(stream):
    """
    :param stream: list
    :return:None
    """

    from datstru import Heap
    class StreamList(object):
        """
        extended heap data structure
        """

        def __init__(self):
            self.left = Heap() # big top
            self.right = Heap(cmp = lambda x,y:x < y) # small top

        def insert(self, n):
            if len(self) % 2:
                if self.right and n > self.right.top():
                    self.right.insert(n)
                    self.left.insert(self.right.pop())
                else:
                    self.left.insert(n)
            else:
                if self.left and n < self.left.top():
                    self.left.insert(n)
                    self.right.insert(self.left.pop())
                else:
                    self.right.insert(n)
            return

        def get_median(self):
            if len(self) % 2:
                return self.right.top()
            else:
                return (self.left.top() + self.right.top()) / 2

        def __len__(self):
            return len(self.left) + len(self.right)

    con = StreamList()
    for n in stream:
        con.insert(n)
        print(con.get_median())
    return

stream_median([1,2,6,5,3,2,3,5,7,9])