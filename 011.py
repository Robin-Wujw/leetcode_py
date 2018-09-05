# coding=utf-8
import sys
class Solution(object):
    def maxArea(self,height):
        """
        :type height:List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        maxSize = 0
        l       = len(height)
        high       = l-1
        low        = 0
        while(low<high):
            maxSize=max(maxSize,min(height[high],height[low])*(high-low))
            if height[low]<height[high:
                low += 1
            else:
                high-= 1
        return maxSize
def main():
    b=[10,14,10,4,10,2,6,1,6,12]
    a=Solution()
    print(a.maxArea(b))

main()