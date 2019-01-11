"""
面试题27：二叉树的镜像
题目：请完成一个函数，输入一棵二叉树，该函数输出它的镜像。
例：
        8                8
       / \              / \
      6  10            10  6
     / \ / \          / \ / \
    5  7 9  11       11 9 7  5
"""


def mirror_of_binary_tree(root):
    """
    :param root: root
    :return: mirror tree root
    """
    if not root:
        return
    root.left, root.right = root.right, root.left
    mirror_of_binary_tree(root.left)
    mirror_of_binary_tree(root.right)
    return root