# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 0:
#             return  ""
#         elif len(strs) ==1:
#             return strs[0]
#         else:
#             result = strs[0]
#             for i in range(1,len(strs)):
#                 result = self.lcp(result,strs[i])
#             return result


#     def lcp(self,short,long):
#         if(len(short)>len(long)):
#             short,long=long,short
#         for i in range(0,len(short)):
#             if short[i] != long[i]:
#                 return short[:i]
#         return short

# # Method 1: min、max的使用:
# def longestCommonPrefix(self, strs):
#     if not strs: return ""
#     s1 = min(strs)
#     s2 = max(strs)
#     for i,x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1
# # Method 2: zip set的使用:
# def longestCommonPrefix(self, strs):
#     if not strs: return ""
#     ss = list(map(set, zip(*strs)))
#     res = ""
#     for i, x in enumerate(ss):
#         x = list(x)
#         if len(x) > 1:
#             break
#         res = res + x[0]
#     return res
class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs)==0:
            return res 
        if strs[0]=="":
            return strs[0]
        if len(strs)==1:
            return strs[0]
        le = len(strs[0])
        for i in range(le):
            for j in range(1,len(strs)):
                if(len(res)<len(strs[j])):  
                    flag = (strs[0][i] == strs[j][i])
                else:
                    flag = False
                    return res
                if flag == False:
                    return res
            if flag == True:
                res = res + strs[0][i]
            else:
                return res 
        return res
if __name__ == "__main__":
    s = Solution()
    strs = ["cc","acc","ccc"]
    print(s.longestCommonPrefix(strs))