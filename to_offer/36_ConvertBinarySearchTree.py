"""
面试题36：二叉搜索树与双向链表
题目：输入一棵二叉树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何
新的节点，只能调整树种节点指针的指向。

例：
输入：
            10
           /  \
          6    14
         / \   / \
        4   8 12  16
输出：
4<->6<->8<->10<->12<->14<->16
"""

def convert_binary_search_tree(root):
    """
    :param root: binary search tree root
    :return: list node head
    """

    def inorder_convert(node, last_node):
        """
        :param node: current node
        :param last_node: subtree's list head connect to this node
        :return: list end
        """
        if not node:
            return None
        # left tree
        if node.left:
            last_node = inorder_convert(node.left, last_node)
        # root
        node.left = last_node
        if last_node:
            last_node.right = node
        last_node = node
        # right tree
        if node.right:
            last_node = inorder_convert(node.right, last_node)
        return last_node # end of list node

    if not root:
        return None
    head = inorder_convert(root, None)
    while head.left:
        head = head.left
    return head

from datstru import list_to_treenode
root = list_to_treenode([5, 'null',4,'null',3,'null',2,'null',1])
head = convert_binary_search_tree(root)

print()
