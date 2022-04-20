#给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#返回删除后的链表的头节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        headN = ListNode(0)
        headN.next = head 
        Node  = headN
        while(Node.next.val!=val):
            Node = Node.next 
        Node.next = Node.next.next   
        return headN.next