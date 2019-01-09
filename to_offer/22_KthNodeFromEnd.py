"""
面试题22：链表中导数第K个节点
题目：输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始
计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1->2->3->4->5->6
倒数第3个节点，是值为4的节点。
"""

def kth_node_from_end(head, k):
    """
    :param head: head of listnode
    :param k: kth from end
    :return: node
    """
    if head:
        slow = fast = head
    else:
        raise Exception('EMPTY INPUT')

    for i in range(k):
        if fast:
            fast = fast.next
        else:
            raise Exception("K Out Of Range")

    while fast:
        fast = fast.next
        slow = slow.next

    return slow