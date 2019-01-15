"""
面试题35：复杂链表的复制
题目:请实现函数ComplexListNode* Clone(ComplexListNode* pHead),复制一个
复杂链表。在复杂链表中除了有一个m_pNext指针指向下一个节点，还有一个m_pSaibling
指针指向链表中的任意节点或者nullptr。
"""

class ComplexListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None
        self.sibling = None

def complex_list_node_clone(head):
    """
    :param head: origin head
    :return:copy head
    """
    sham_head = ComplexListNode(0)
    new_node = sham_head
    node = head
    reflect = {}
    while node:
        new_node.next = ComplexListNode(node.val)
        new_node = new_node.next
        reflect[node] = new_node
        node = node.next
    node = head
    new_node = sham_head.next
    while node:
        if node.sibling:
            new_node.sibling = reflect[node.sibling]
        node = node.next
        new_node = new_node.next
    return sham_head.next

def complex_list_node_clone_2(head):
    """
    :param head: origin head
    :return:copy head
    """
    node = head
    while node:
        new_node = ComplexListNode(node.val)
        node.next, node = new_node, node.next
        new_node.next = node
    node = head
    while node:
        if node.sibling:
            node.next.sibling = node.sibling.next
        node = node.next.next
    node = head
    copy_head = head.next
    while node.next:
        node.next, node = node.next.next, node.next
    return copy_head