from datstru import TreeNode
def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """

    def recursion(in_start, in_end, post_start, post_end):
        if post_start > post_end:
            return None
        val = postorder[post_end]
        root = TreeNode(val)
        in_i = in_index[val]
        post_i = in_i - in_start + post_start -1
        root.left = recursion(in_start, in_i - 1, post_start, post_i)
        root.right = recursion(in_i + 1, in_end, post_i + 1, post_end - 1)
        return root

    if not inorder or not postorder:
        return None
    else:
        in_index = {value: index for index, value in enumerate(inorder)}
        return recursion(0, len(inorder) - 1, 0, len(postorder) - 1)

inorder =[9,3,15,20,7]
postorder = [9,15,7,20,3]

root = buildTree(inorder, postorder)
print()