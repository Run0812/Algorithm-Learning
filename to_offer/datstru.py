class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None

def list_to_listnode(input):
    """
    Generate list from the input
    :param input: val list
    :return: head of ListNode
    """
    numbers = input
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_treenode(input):
    # input = input.strip()
    # input = input[1:-1]
    if not input:
        return None
    # inputValues = [s.strip() for s in input.split(',')]
    inputValues = input
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Heap(object):
    """
    Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k, counting elements FROM 1.
    To DISTINGUISH from LIST: Heap.data[0] = 'HEAP'。
    Usage:
    h = Heap()                                      # create an empty big top heap
    h = Heap(data)                                  # create an big top heap with init data in LIST
    h = Heap(cmp = lambda x,y:x < y)                # create an empty small top heap
    heap.insert(item)                               # insert an new element
    top_element = heap.top()                        # see the top element
    top_element = heap.pop()                        # pop out the top element
    """

    def __init__(self, data = [], cmp = lambda x,y:x > y):
        """
        :param cmp: keys comparison Func
        :param data: List
        """
        self._cmp = cmp
        if isinstance(data, list):
            self.data = ['HEAP'] + data
        else:
            raise Exception('Data Arg Must Be List')
        self.len = len(self.data) - 1
        self._buildup()

    # TODO: modify element's key in heap

    def _buildup(self):
        # TODO: build up heap from a list
        for i in range(self.len >> 1, 0, -1):
            self._shift_dn(i)
        return


    def insert(self, elements):
        # TODO: func1 - insert single elements
        # TODO: func2 - insert elements in list
        for ins_elt in elements:
            self.data.append(ins_elt)
            self.len += 1
            self._shift_up(self.len)
        return

    def _shift_up(self, i):
        parent = i >> 1
        while parent > 0:
            if self._cmp(self.data[i], self.data[parent]):
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
                parent = i >> 1
            else:
                break
        return

    def _shift_dn(self, i):
        req = i
        left = i << 1
        right = (i << 1) + 1
        if left <= self.len and self._cmp(self.data[left],self.data[req]):
            req = left
        if right <= self.len and self._cmp(self.data[right],self.data[req]):
            req = right
        if req != i:
            self.data[req], self.data[i] = self.data[i], self.data[req]
            self._shift_dn(req)
        return

    def top(self):
        return self.data[1]

    def pop(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        pop_elt = self.data.pop()
        self.len -= 1
        self._shift_dn(1)
        return pop_elt

    def __len__(self):
        return len(self.data) - 1