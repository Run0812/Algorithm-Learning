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