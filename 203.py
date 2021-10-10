# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        H = ListNode(next=head)
        cur = H 
        while(cur.next!=None):
            if(cur.next.val == val ):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return H.next