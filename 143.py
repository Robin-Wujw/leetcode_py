# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        给定一个单链表 L 的头节点 head ，单链表 L 表示为：
         L0 → L1 → … → Ln-1 → Ln 
        请将其重新排列后变为：
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        """
        queue = collections.deque()
        temp = head
        while temp.next:
            queue.append(temp.next)
            temp = temp.next
        temp = head
        while len(queue):
            temp.next = queue.pop()
            temp = temp.next 
            if(len(queue)):
                temp.next = queue.popleft()
                temp = temp.next 
        temp.next = None