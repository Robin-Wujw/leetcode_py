# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
# 题目数据 保证 整个链式结构中不存在环。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        curA = headA
        curB = headB 
        while(curA!=None):
            lenA += 1
            curA = curA.next
        while(curB!=None):
            lenB += 1
            curB = curB.next  
        num = lenA-lenB
        while(headA!=None):
            if(num>0):
                if(num!=0):
                    headA = headA.next
                    num   -= 1
                else:
                    if(headA.val == headB.val):
                        return headA
                    headA = headA.next 
                    headB = headB.next
            else:
                if(num!=0):
                    headB = headB.next 
                    num   -= 1 
                else:
                    if(headA.val == headB.val):
                        return headB
                    headA = headA.next 
                    headB = headB.next          
        return None

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # 当一个链表走完了就去走另一个链表的路
    #     cur1, cur2 = headA, headB

    #     while cur1 != cur2:
    #         cur1 = cur1.next if cur1 else headB
    #         cur2 = cur2.next if cur2 else headA
    #     return cur1