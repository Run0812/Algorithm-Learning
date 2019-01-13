"""
面试33：二叉搜索树的后序遍历序列
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后续遍历结果，如果是则返回
True，否则返回False。假设输入的数组的任意两个数字都互不相同。
例：
输入数组[5, 7, 6, 9, 11, 10, 8]， 则返回True。因为这个整数序列是下树的后序遍历。
         8
      /     \
     6       10
    / \     /  \
   5   7   9    11
如果输入的数组是[7, 4, 6, 5]，则由于没有那棵二叉搜索树的后序遍历结构是这个序列，
因此返回False。
"""
# TODO: check in O(n) during return
def sequence_of_bst(postorder):
    """
    :param postorder: LRD of binary search tree
    :return: bool
    """
    if len(postorder) <= 1:
        return True
    root =  postorder[-1]
    # right_child = postorder.filter(lambda x: x > root, postorder)
    # left_child = postorder.filter(lambda x: x < root, postorder)
    count = 0
    for node in postorder[:-1]:
        if  node < root:
            count += 1
        else:
            break
    right_child = postorder[count:-1]
    left_child = postorder[:count]
    for node in right_child:
        if node < root:
            return False
    if left_child:
        left = sequence_of_bst(left_child)
    else:
        return True
    if right_child:
        right = sequence_of_bst(right_child)
    else:
        return True
    return left and right

print(sequence_of_bst([4, 6, 12, 8, 16, 14, 10]))