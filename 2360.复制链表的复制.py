"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head ==None:
            return []
        cur = head 
        dict= {}
        while cur:
            dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head 
        while cur:
            dict[cur].next = dict.get(cur.next)
            dict[cur].random = dict.get(cur.random)
            cur = cur.next 
        return dict[head]