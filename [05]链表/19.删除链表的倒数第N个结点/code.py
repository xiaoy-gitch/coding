# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(next=head)  #设置哨兵结点避免出现删除头节点的情况
        for _ in range(n):
            right = right.next
        while right.next:  #right走到最后一个结点结束
            right = right.next
            left = left.next
        #找到了倒数第n+1个结点
        left.next = left.next.next
        return dummy.next 
