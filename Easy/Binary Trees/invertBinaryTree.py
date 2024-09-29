""" Given the root of a binary tree, invert the tree, and return its root. """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        else: 
            root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
"""     Explanation:

	1.	Base Case Check: The function first checks if root is None. 
    If so, it returns None, preventing attempts to access left or right attributes on a NoneType.
	2.	Swap Left and Right Children: The left and right children of the current node are swapped using 
    Python’s multiple assignment feature: root.left, root.right = root.right, root.left.
	3.	Recursive Inversion: The function then recursively calls itself on the left and right subtrees 
    to continue swapping nodes deeper in the tree.
	4.	Return the Root: After inverting all nodes, the root of the inverted tree is returned. """