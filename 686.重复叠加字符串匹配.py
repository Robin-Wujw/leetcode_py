#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #如果b中有a中没有的元素，肯定不可能
        result=''
        cnt=0
        while b not in result: 
            cnt+=1
            result+=a
            #分析可以发现，b/a+2一定是a叠加的上限    
            if cnt > len(b)/len(a)+2:
                return -1
            
        return cnt
# @lc code=end

