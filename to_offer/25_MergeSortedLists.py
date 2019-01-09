"""
面试题25：合并两个排序的链表
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然使递增排序的。
例：
L1:1->3->5->7
L2:2->4->6->8
L:1->2->3->4->5->6->7->8
"""

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None

def merge_sorted_lists( l1, l2):
    """
    :param l1: ListNode 1 head
    :param l2: ListNode 2 head
    :return: merged L head
    """
    if not l1 or not l2:
        return l1 or l2
    if l1.val <= l2.val:
        main = l1
        sub = l2
    else:
        main = l2
        sub = l1
    last = main
    while sub and last.next:
        if last.next.val <= sub.val:
            pass
        else:
            temp = last.next
            last.next = sub
            sub = temp
        last = last.next
    last.next = sub
    return main

def merge_sorted_lists_2(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    sham_head = ListNode(0)
    sham_head.next = l1
    node = sham_head
    while node.next:
        if node.next.val > l2.val:
            node.next, l2 = l2, node.next
        node = node.next
    node.next = l2
    return sham_head.next

def merge_sorted_lists_3(l1, l2):
    sham_head = ListNode(0)
    node = sham_head
    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 or l2
    return sham_head.next