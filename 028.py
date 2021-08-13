class Solution:
    def strStr(self, haystack, needle):
        '''
        给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
        '''
#-超时结果-#       
        # if needle == '' or not needle:  
        #     return 0
        # first = -1 
        # flag = False
        # for i in range(len(haystack)-len(needle)+1):
        #     Flag = True
        #     for j in range(len(needle)):
        #         if haystack[i+j]!=needle[j]:
        #             Flag=False
        #             break
        #         if Flag:
        #             for a in range(len(needle)):
        #                 if haystack[i+a] == needle[a]:
        #                     flag = True
        #                 else:
        #                     flag = False
        #                     break
        #             if(flag == True):
        #                 first = i
        #                 return first
        # return first
#-取巧方法-#
        # if needle == '' or not needle:
        #     return 0
        # for i in range(len(haystack)):
        #     if i + len(needle) > len(haystack):
        #         return -1
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
#-Kmp方法-#
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        next=self.getnext(a,needle)
        p=-1
        for j in range(b):
            while p>=0 and needle[p+1]!=haystack[j]:
                p=next[p]
            if needle[p+1]==haystack[j]:
                p+=1
            if p==a-1:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next=['' for i in range(a)]
        k=-1
        next[0]=k
        for i in range(1,len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k=next[k]
            if needle[k+1]==needle[i]:
                k+=1
            next[i]=k
        return next
if __name__ ==  "__main__":
    s = Solution()
    haystack = "mississippi"
    needle = "aabacaab"
    print(s.strStr(haystack,needle))