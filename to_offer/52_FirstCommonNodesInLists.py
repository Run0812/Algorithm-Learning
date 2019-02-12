"""
面试题52：两个链表的第一个公共节点
题目：输入两个链表，找出它们的第一个公共节点。

例：
1->2->3
        \
          >6->7
        /
    4->5
公共节点为6。
"""

def first_common_nodes_in_lists(headA, headB):
    """
    :param headA: ListNode 1 head
    :param headB: ListNode 2 head
    :return: intersection node
    """
    if not headA or not headB:
        return None
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1