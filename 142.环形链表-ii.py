#
# @lc app=leetcode.cn id=142 lang=python3
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:  return None
        slow = fast = head 
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if(fast == slow):
                cur1 = head
                cur2 = fast
                while(cur1 != cur2):
                    cur1 = cur1.next
                    cur2 = cur2.next        
                return cur1
        return None
        
# @lc code=end

