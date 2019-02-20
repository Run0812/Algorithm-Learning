"""
面试题55:二叉树的深度
题目1：二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点一次经过的节点
形成树的一条路径，从最长路径的长度为树的深度。

例：
        1
       / \
      2   3
     / \   \
    4   5   6
       /
      7
深度为4。
"""


def depth_of_tree(root):
    """
    :param root: tree root
    :return: height of tree
    """
    if not root:
        return 0
    left = depth_of_tree(root.left)
    right = depth_of_tree(root.right)
    return max(left, right) + 1

from datstru import list_to_treenode
tree = list_to_treenode([1,2,3,4,5,'null',6,'null','null',7])
print(depth_of_tree(tree))