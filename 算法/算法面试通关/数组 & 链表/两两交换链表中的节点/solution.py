# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        pre, cur = dummy, head
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt
            pre = cur
            cur = cur.next
        return dummy.next