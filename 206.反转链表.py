#
# @lc app=leetcode.cn id=206 lang=python3
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None 
        cur = head
        while(cur!=None):
            temp = cur.next
            cur.next = pre 
            pre = cur 
            cur = temp 
        return pre
            
# @lc code=end

