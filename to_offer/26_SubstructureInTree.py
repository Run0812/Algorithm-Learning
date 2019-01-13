"""
面试题26：树的子结构
题目：输入两棵二叉树A和B，判断B是不是A的子结构。
例：
                A                      B
                8                      8
            /       \                /   \
           8         7              9     2
         /   \
        9     2
            /   \
           4     7

A树中有一部分子树和B是一样的，因此B是A的子结构。
"""

from datstru import TreeNode

def substrucure_in_tree(main, sub):
    """
    :param main: Big Tree
    :param sub: substructure
    :return: bool
    """

    def compare(main_tree_sub, sub):
        """
        :param main_tree_sub: node
        :param sub: substructure_root
        :return: bool
        """
        if not sub:
            return True
        if not main_tree_sub:
            return False
        if sub.val == main_tree_sub.val:
            return compare(main_tree_sub.left, sub.left) and compare(main_tree_sub.right, sub.right)
        return False

    if not main:
        return False
    if main.val == sub.val and compare(main, sub):
        return True
    else:
        return substrucure_in_tree(main.left, sub) or substrucure_in_tree(main.right, sub)
    return


def substrucure_in_tree_2(main, sub):
    def preorder(root):
        return (root.val, preorder(root.left), preorder(root.right)) if root else None
    return str(preorder(sub)) in str(preorder(main))


a = TreeNode(123)
print(str(a))