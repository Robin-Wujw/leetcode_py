# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        head_i = ListNode(0)
        head_i.next = head
        pre = head_i 
        while head_i.next and head_i.next.next:
            tmp = head_i.next.next
            head_i.next.next = head_i.next.next.next
            tmp.next = head_i.next
            head_i.next = tmp
            head_i = head_i.next.next
        return pre.next



if __name__ == "__main__":
    s = Solution()
    head = [1]
    pre = l1 = ListNode(head[0])
    for i in range(1,len(head)):
        l1.next = ListNode(head[i])
        l1 = l1.next
    print(s.swapPairs(pre))