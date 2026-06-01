# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left:int,right:int)->Optional[TreeNode]:
            if left>right:
                return None
            best =left
            for i in range(left+1,right+1):
                if nums[i]>nums[best]:
                    best =i
            node = TreeNode(nums[best])
            node.left =construct(left,best-1)
            node.right =construct(best+1,right)
            return node
        return construct(0,len(nums)-1)
#方法2：单调栈来做。。。
