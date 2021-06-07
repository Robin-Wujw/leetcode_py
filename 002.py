# class Solution(object):
# 	def addTwoNumbers(self,l1,l2):
# 		root = ListNode(0)		
# 		result = root
# 		carry = 0	
# 		while l1 or l2 or carry == 1:
# 			value = 0
# 			if l1:
# 					value += l1.val
# 					l1 = l1.next
# 			if l2:
# 					value += l2.val
# 					l2    = l2.next
# 			value += carry
# 			root.next = ListNode(value %10)
# 			carry = int(value/10)
# 			root = root.next
# 		return result.next

#123+234 = 357
#321+432 = 753 
#673+587 = 
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def addTwoNumbers(self, l1, l2):
		result = ListNode()
		head = result
		carry = 0
		while l1 or l2 or carry==1:#l1 or l2值存在or存在进位(最高位进位)
			value = 0 #value 表示result中某位的值
			if l1:
				value += l1.val
				l1 = l1.next
			if l2:
				value += l2.val
				l2 = l2.next
			value += carry 
			carry = int(value/10)# 进位
			result.next = ListNode(value%10) #某位的值
			result = result.next
		return head.next
if __name__ == "__main__":
	So = Solution()
	l1 = ListNode(4)
	l1.next = ListNode(6)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	result = So.addTwoNumbers(l1,l2)
	while(result):
		print(result.val)
		result = result.next


