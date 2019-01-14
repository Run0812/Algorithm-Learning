"""
面试题34：二叉树中和为某一值的路径
题目：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

例：
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

打印：
   [5,4,11,2],
   [5,8,4,5]
"""

def path_in_tree(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    def recursion_core(node, sum):
        """
        :param node:subtree root
        :param sum: sub sum
        :return: [path(list)] if has path else []
        """
        if not node.left and not node.right:
            subpath = [[]] if sum == node.val else []
        else:
            subpath_l = recursion_core(node.left, sum - node.val) if node.left else []
            subpath_r = recursion_core(node.right, sum - node.val) if node.right else []
            subpath = subpath_l + subpath_r
        return [[node.val] + path for path in subpath]

    if not root: return []
    return print(recursion_core(root, sum))
