# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def recursion_core(node, sum):
            if not node.left and not node.right:
                subpath = [[]] if sum == node.val else []
            else:
                subpath_l = recursion_core(node.left, sum - node.val) if node.left else []
                subpath_r = recursion_core(node.right, sum - node.val) if node.right else []
                subpath = subpath_l + subpath_r
            return [[node.val] + path for path in subpath]

        if not root: return []
        return recursion_core(root, sum)