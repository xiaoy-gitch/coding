# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans =[]
        stack =[]
        cur =head
        idx =-1
        while cur:
            idx +=1
            ans.append(0)
            while stack and cur.val>stack[-1][0]:
                ans[stack[-1][1]] =cur.val
                stack.pop()
            stack.append((cur.val,idx))
            cur =cur.next
        return ans 
