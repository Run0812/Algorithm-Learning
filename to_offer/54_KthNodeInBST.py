"""
面试题：二叉搜索树的第K大节点
题目：给定一棵二叉搜索树，请找出其中第k大的节点。

例：
如下图的二叉搜索树，按节点数值大小顺序，第三大节点是4。
        5
       / \
      3   7
     / \ / \
    2  4 6  8
"""


def kth_node_in_BST(root, k):
    """
    :param root: Binary Search Tree root
    :param k: kth smallest
    :return: kth smallest node
    """

    def recursion(root, k):
        nonlocal target
        if not root:
            return k
        k = recursion(root.left, k)
        if not target:
            if k == 1:
                target = root
            else:
                k -= 1
        if not target:
            k = recursion(root.right, k)
        return k
    target = None
    recursion(root, k)
    return target

from datstru import list_to_treenode
tree = list_to_treenode([8,6,10,5,7,9,11])
k = 1
ans = kth_node_in_BST(tree, k)
print()
