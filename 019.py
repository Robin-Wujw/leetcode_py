# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        '''
        输入：head = [1,2,3,4,5], n = 2
        输出：[1,2,3,5]
        '''
        head_i  = ListNode()# 先设个空白头节点
        head_i.next = head
        fast,slow = head_i,head_i
        i = 1
        while(fast.next!=None):
            fast = fast.next
            if(i>n):
                slow = slow.next
            i = i+1
        if(n==1):
            slow.next=None
        else:
            slow.next = slow.next.next #删除
        return head_i.next
if __name__ == "__main__":
    s = Solution()
    head = [1]
    pre = l1 = ListNode(head[0])
    for i in range(1,len(head)):
        l1.next = ListNode(head[i])
        l1 = l1.next
    n = 1
    print(s.removeNthFromEnd(pre,n))