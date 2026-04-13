# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #如果二者有交点，会在交点处相遇，如果没有会同时指向null
        p,q = headA,headB
        while p!=q:
            if p:
                p=p.next
            else:
                p=headB
            if q:
                q=q.next
            else:
                q=headA
        return p      
