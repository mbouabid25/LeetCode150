""" Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children. """


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        targetSum -= root.val
        if root.right is None and root.left is None and targetSum == 0:
            return True
            
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
    
""" Base Case: If the root is None, the function returns False because there's no path to check.
Recursive Step: At each node, you subtract the node's value from targetSum. Then:
If it's a leaf node (both left and right children are None), check if targetSum equals 0. If it does, 
you've found a valid path and return True.
Otherwise, recursively check both the left and right subtrees. 
The function returns True if either subtree has a valid path (or condition).
This process continues until either a valid path is found or all possible paths are explored. """

""" Time Complexity:
O(N), where N is the number of nodes in the tree.
In the worst case, the algorithm must visit every node exactly once to determine whether a valid path exists.

Space Complexity:
O(H), where H is the height of the tree.
The space complexity comes from the recursion stack, which can be at most the height of the tree.
In the worst case (when the tree is skewed and acts like a linked list), the height is O(N). In the best case (a balanced tree), the height is O(log N). """
