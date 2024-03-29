#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#

# @lc code=start
class Node:
    def __init__(self, key="", count=0): #node会存储计数为count的 节点和，存储在keys中
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node: 'Node') -> 'Node':  # 在 self 后插入 node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):  # 从链表中移除 self
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root  # 初始化链表哨兵，下面判断节点的 next 若为 self.root，则表示 next 为空（prev 同理）
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:  # key 不在链表中
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1)) #如果链表为空 或者下一个node的count大于1  则从开头加进去
            else: #链表不为空 或者 root的下一个count=1 则在root下一个node里加进key
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else: # key在链表中
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1: #下一个是结尾 或者下一个的count大于 count+1 则要添加一个count+1的node
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else: #否则就在下一个node加上key 然后将原来的keys中去掉key
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0: #如果原来的keys里没key了就删去
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:  # key 仅出现一次，将其移出 nodes
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count < cur.count - 1: 
                self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
                #在pre后添加
            else: # cur 前面有node 或 pre的node.count 等于 cur.count-1   就要往前添加
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

