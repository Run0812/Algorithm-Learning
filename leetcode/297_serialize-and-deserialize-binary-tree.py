# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from datstru import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        l_node = [root]
        seq = []
        ni = 0
        while ni < len(l_node):
            cur = l_node[ni]
            if cur:
                seq.append(str(cur.val))
                l_node.extend([cur.left, cur.right])
            else:
                seq.append('null')
            ni += 1
        return '[' + ','.join(seq) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        root_val = data[0]
        if root_val == 'null':
            return []
        else:
            root = TreeNode(root_val)
        node = [root]
        di = 1
        ni = 0
        while di < len(data):
            cur = node[ni]
            if cur:
                val_l = data[di]
                val_r = data[di + 1]
                cur.left = TreeNode(int(val_l)) if val_l != 'null' else None
                cur.right = TreeNode(int(val_r)) if val_r != 'null' else None
                node.extend([cur.left, cur.right])
                di += 2
            ni += 1
        return root