""" Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3 """



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None : 
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right)+1
        
""" Explanation of the Code:
Base Case: If the root is None, it returns 0 because there's no tree.
Recursive Calculation: It calculates the depth of the left and right subtrees recursively.
Depth Calculation: It returns the maximum of the left and right subtree depths plus 1 (accounting for the current node).
In the example [3,9,20,null,null,15,7], the maximum depth is 3, 
corresponding to the path from the root (3) down to the leaf nodes (9 or 7). """