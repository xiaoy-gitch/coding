# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        r1=head
        while r1:
            r2=r1.next
            r1.next=pre
            pre=r1
            r1=r2
        return pre
