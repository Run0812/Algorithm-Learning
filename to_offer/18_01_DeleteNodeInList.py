"""
面试题18：删除链表的节点
题目1：在O(1)的时间内删除链表节点。
给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
链表节点定义如下：
"""
class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def delete_ListNode(head, delete_node):
    """
    :param head: head of NodeList
    :param delete_node: node
    :return: head
    """
    next_node = delete_node.next
    if next_node:
        # not del end
        delete_node.val, next_node.val = next_node.val, delete_node.val
        delete_node.next = next_node.next
    elif head is not delete_node:
        # del end
        while head.next is not delete_node:
            head = head.next
        head.next = None
    else:
        # delete head
        head = None
    return head

a = ListNode(1)

delete_ListNode(a,a)

