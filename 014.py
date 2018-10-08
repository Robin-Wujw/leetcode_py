class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return  ""
        elif len(strs) ==1:
            return strs[0]
        else:
            result = str[0]
            for i in range(1,len(strs)):
                result = self.lcp(result,strs[i])
            return result


    def lcp(self,short,long):
        if(len(short)>len(long)):
            short,long=long,short
        for i in range(0,len(short)):
            if short[i] != long[i]:
                return short[:i]
        return short

