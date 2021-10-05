# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if(not headA or not headB):
            return None
        h_a,h_b = headA,headB
        while(h_a!=h_b):
            h_a = headB if h_a == None else h_a.next
            h_b = headA if h_b == None else h_b.next
        return h_a