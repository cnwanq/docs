# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        start, end = head, head
        for i in range(k):
            if not end:
                return head
            end = end.next
        newHead = self.reverse(start, end)
        start.next = self.reverseKGroup(end, k)
        return newHead
    
    def reverse(self, start: ListNode, end: ListNode) -> ListNode:
        pre, cur, nxt = None, start, start
        while cur!= end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        