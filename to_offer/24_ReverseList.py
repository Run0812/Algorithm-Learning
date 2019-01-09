"""
面试题24：反转链表
题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
例如:
输入：1->2->3->4->5->None
输出：5->4->3->2->1->None
"""

def reverse_list(head):
    """
    :param head: head
    :return: new head
    """
    node = head
    pre = None
    while node:
        node.next, pre, node = pre, node, node.next
    return pre