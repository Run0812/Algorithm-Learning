"""
面试题6:从尾到头打印链表
题目：输入一个链表的头节点，从尾到头反过来打印出每个节点的值。链表节点定义如下：

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None
例：1->2->3->4->5
    输出5 4 3 2 1
"""
from datstru import ListNode
from datstru import list_to_listnode

def print_list_in_reversed(head):
    """
    :param head: ListNode head
    :return: None
    """
    def print_list_in_re(head):
        if head:
            print_list_in_re(head.next)
            print(head.val)
        return
    if head:
        # empty input check
        print_list_in_re(head)
    else:
        print('EMPTY INPUT')
    return

def print_list_in_reversed_2(head):
    """
    :param head: ListNode head
    :return: None
    """
    val_print_reversed = []
    if not head:
        # empty input check
        val_print_reversed.append('EMPTY INPUT')
    while head:
        val_print_reversed.append(head.val)
        head = head.next
    print(val_print_reversed[::-1])
    return



head = list_to_listnode([1,2,3,4,5])
print_list_in_reversed_2(head)