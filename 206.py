class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur  = head 
        while(cur!=None):
            n_temp = cur.next
            cur.next = prev
            prev = cur 
            cur = n_temp
        return prev 
        #高效方法
        # """
        # :type head: ListNode
        # :rtype: ListNode
        # """
        # p, rev = head, None
        # while p:
        #     rev, rev.next, p = p, rev, p.next
        # return rev