"""
面试题55:二叉树的深度
题目2：平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左、右子树的深度相差不超过1，
那么它就是一棵平衡二叉树。
"""


def is_balanced(root):
    """
    :param root:binary tree root
    :return: is balanced
    """
    def core(root):
        if not root:
            return 0
        left = core(root.left)
        right = core(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)

    return core(root) != -1