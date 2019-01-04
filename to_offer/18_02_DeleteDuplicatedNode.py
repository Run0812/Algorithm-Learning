"""
面试题18：删除链表的节点
题目2：删除链表中重复的节点
在一个排序后的链表中，如何删除重复的节点？
例：
输入: 1->1->2->3->3
输出: 1->2->3
"""
def delete_duplicated_node(head):
    """
    :param head: head of ListNode
    :return: head
    """
    cur = head
    pre = None
    while cur:
        pre = cur
        cur = cur.next
        while cur and cur.val == pre.val:
            cur = cur.next
        pre.next = cur
    return head


