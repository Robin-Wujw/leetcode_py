class Solution:
    def isIsomorphic(self, s, t):
        return all(s.index(s[i])==t.index(t[i]) for i in range(len(s)))
        list = {}
        for i in range(len(s)):
            if(s[i] not in list):
                list[s[i]] = t[i]
            else:
                if(t[i]!=list[s[i]]):
                    return False
        list.clear()
        for i in range(len(t)):
            if(t[i] not in list):
                list[t[i]] = s[i]
            else:
                if(s[i]!=list[t[i]]):
                    return False
        return True
if __name__ ==  "__main__":
    a = Solution()
    s = "badc"
    t = "baba"
    print(a.isIsomorphic(s,t))