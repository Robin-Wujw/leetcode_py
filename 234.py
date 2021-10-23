class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        length = 0
        temp = head 
        while(temp):
            length+=1
            temp = temp.next 
        result = [0] * length
        for i in range(length):
            result[i] = head.val
            head = head.next 
        i = 0 
        j = length - 1
        while(i<j):
            if(result[i]==result[j]):
                i += 1
                j -= 1
            else:
                return False
        return True
