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
                pointer = max(Dict[value],pointer)
            maxLen = max(index-pointer+1 ,maxLen)
            Dict[value] = index
        print(Dict)
        print(maxLen)
# aabcadwe 
# 1. a:0 maxLen=1 2.pointer=0 maxLen=
if __name__ == "__main__":
    So = Solution()
    s = "aa"
    So.lengthOfLongestSubstring(s)