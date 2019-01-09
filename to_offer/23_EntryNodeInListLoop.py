"""
面试题23：链表中的入口节点
题目：如果一个链表中包含环，如何找出环的入口节点？
例如：
1->2->3->4->5->6
   个__________|
"""

def entry_node_in_list_loop(head):
    """
    :param head: head
    :return: entry node
    """
    pos = None
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            pos = head
            while pos is not slow:
                pos = pos.next
                slow = slow.next
            break
    return pos