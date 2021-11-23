#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = slow = fast = ListNode(next=head)
        num = 0
        while(fast.next!=None):
            fast = fast.next
            num = num + 1
            if(num >= n + 1):
                slow = slow.next 
        slow.next = slow.next.next 
        return cur.next 
# @lc code=end

