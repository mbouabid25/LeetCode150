""" Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # Base Case 1: Both nodes are None
        if not p and not q:
            return True
        
        # Base Case 2: One node is None, the other is not
        if not p or not q:
            return False
        
        # Base Case 3: Both nodes exist but have different values
        if p.val != q.val:
            return False
        
        # Recursively check the left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

