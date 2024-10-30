# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq,depth = deque([root]), 1
        while dq:
            for i in range(len(dq)):
                tmp = dq.popleft()
                if not tmp.left and not tmp.right:
                    return depth
                if tmp.left:
                    dq.append(tmp.left)
                if tmp.right:
                    dq.append(tmp.right)
            depth += 1
        return depth