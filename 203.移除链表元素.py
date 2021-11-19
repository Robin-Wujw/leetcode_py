#
# @lc app=leetcode.cn id=203 lang=python3
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if head == None: return head
        # if head.val == val:
        #     head = head.next
        # temp = head
        # while(head.next!=None):
        #     if(head.next.val==val):
        #         head.next = head.next.next
        #     else:
        #         head = head.next 
        # return temp  
        while head is not None and head.val==val: #保证链表第一个节点的值不等于val
            head=head.next
        if not head:         #判断链表是否为空
            return None
        headNode = head     #头节点
        while head.next is not None:
            if head.next.val==val:
                head.next = head.next.next
            else:
                head=head.next
        return headNode
        # H = ListNode(next=head)
        # temp = H 
        # while(temp.next!=None):
        #     if(temp.next.val==val):
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next 
        # return H.next
# @lc code=end

