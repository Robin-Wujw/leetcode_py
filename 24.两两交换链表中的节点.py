#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
        # if head == None or head.next == None:
        #     return head 
        # N = ListNode(next=head)
        # temp = N
        # while temp.next and temp.next.next:
        #     pre = temp.next
        #     cur = temp.next.next
        #     pre.next = cur.next 
        #     cur.next = pre
        #     temp.next = cur
        #     temp = temp.next.next
        # return N.next
        # if(head == None or head.next == None):
        #     return head
        # N = head.next
        # head.next = self.swapPairs(N.next)
        # N.next = head
        # return N
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res
        
        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next
            
            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next

# @lc code=end

