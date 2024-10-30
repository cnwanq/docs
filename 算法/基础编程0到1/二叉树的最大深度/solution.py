# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 二叉树为空，最小高度为 0
        if root == None:
            return 0
        # 只有根节点，最小高度为 1
        if root.left == None and root.right == None:
            return 1
        # 左子树最小值和右子树最小值
        leftMindepth = self.minDepth(root.left)
        rightMindepth = self.minDepth(root.right)

        # 如果节点的左子树不为空，右子树为空
        if root.left != None and root.right == None:
            return leftMindepth + 1
        # 如果节点的右子树不为空，左子树为空
        if root.left == None and root.right != None:
            return rightMindepth + 1
        # 左右子树都不为空
        return min(leftMindepth, rightMindepth) + 1