# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        """
        给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
        说明：不允许修改给定的链表。
        进阶：
        你是否可以使用 O(1) 空间解决此题？
        输入：head = [3,2,0,-4], pos = 1
        输出：返回索引为 1 的链表节点
        解释：链表中有一个环，其尾部连接到第二个节点。
        """
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