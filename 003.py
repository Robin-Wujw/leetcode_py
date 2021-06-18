# class Solution(object):
#     def lengthOfLongestSubstring(self,s):
#         tempDict = {}
#         maxLen   = 0
#         pointer  = 0
#         for index,value in enumerate(s):
#             if value in tempDict:
#                 pointer  = max(tempDict[value] +1 ,pointer)
#             maxLen  =   max(index - pointer +1 ,maxLen)
#             tempDict[value] = index
#         return maxLen
class Solution:
    def lengthOfLongestSubstring(self, s):
        Dict = {}
        maxLen = 0
        pointer = 0
        for index,value in enumerate(s):
            if value in Dict:
                pointer = max(Dict[value]+1,pointer)
            maxLen = max(index-pointer+1 ,maxLen)
            Dict[value] = index
        print(Dict)
        print(maxLen)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
                print(i,s[i],cur_len,lookup,left)
            print(cur_len)
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
        
# aabcadwe 
# 1. a:0 maxLen=1 2.pointer=0 maxLen=
if __name__ == "__main__":
    So = Solution()
    s = "rrasdsw"
    So.lengthOfLongestSubstring(s)