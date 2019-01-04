class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

def stringToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    def listNodeQuickSort(head, end):
        if head.next is end:
            return
        p = head.next
        node = p.next
        pre = p
        while node is not end:
            if node.val < p.val:
                head.next, node.next, node = node, head.next, node.next
                pre.next = node
            else:
                node = node.next
                pre = pre.next
        listNodeQuickSort(head, p)
        listNodeQuickSort(p, end)

    hhead = ListNode('head')
    hhead.next = head
    listNodeQuickSort(hhead, None)
    return hhead.next

def listNodePrint(head):
        while head:
            print(head.val, sep = '->')
            head = head.next
        print('-----')
        return

def sortList2(head):

    def listNodeMerge(p_head,q_head):

        head = ListNode('head')
        p = p_head
        q = q_head
        cur_node = head
        while p and q:
            if p.val <= q.val:
                cur_node.next = p
                p = p.next
            else:
                cur_node.next = q
                q = q.next
            cur_node = cur_node.next
        cur_node.next = p or q
        listNodePrint(head.next)
        return head.next

    def listNodeMergeSort(head):
        if not head.next:
            return head
        mid = end = head
        pre = None
        while end and end.next:
            pre = mid
            mid = mid.next
            end = end.next.next
        pre.next = None
        l = listNodeMergeSort(head)
        r = listNodeMergeSort(mid)
        return listNodeMerge(l, r)

    return  listNodeMergeSort(head)


listNodePrint(sortList2(stringToListNode([1,3,2,4])))