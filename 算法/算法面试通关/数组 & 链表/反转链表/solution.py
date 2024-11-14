# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current = head
        # pre = None
        # while current:
        #     temp = current.next
        #     current.next = pre
        #     pre = current
        #     current = temp
        # return pre
        
        # 递归方式
        # return self.reverse(head, None)

        # 简洁算法
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
            


    # def reverse(self, current: ListNode, pre: ListNode) -> ListNode:
    #     if current == None:
    #         return pre
    #     temp = current.next
    #     current.next = pre
    #     return self.reverse(temp, current)