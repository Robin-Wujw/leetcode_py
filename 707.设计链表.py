#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._count = 0    

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._count:
            return
        elif index < 0:
            self.addAtHead(self,val)
        else:
            self._count += 1
            node = self._head
            next_n = Node(val) #建立新节点
            for i in range(index):
                node = node.next
            next_n.next = node.next
            node.next = next_n
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            node = self._head
            self._count -= 1
            for i in range(index):
                node = node.next 
            node.next = node.next.next
        # if 0 <= index < self._count:
        #     # 计数-1
        #     self._count -= 1
        #     prev_node, current_node = None, self._head
        #     for _ in range(index + 1):
        #         prev_node, current_node = current_node, current_node.next
        #     else:
        #         prev_node.next, current_node.next = current_node.next, None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

