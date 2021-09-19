class Solution:
    def restoreIpAddresses(self, s):
        """
        给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
        有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
        例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
        输入：s = "25525511135"
        输出：["255.255.11.135","255.255.111.35"]
        """
        path = []
        result = []
        def isValid(p):
            if p=='0': return True
            if p[0]=='0': return False
            if int(p)>0 and int(p)<256: return True
            else:return False
        def backtrack(s,startIndex):
            if len(s)>12:return 
            if len(path) == 4 and startIndex == len(s):
                return result.append('.'.join(path[:]))
            for i in range(startIndex,len(s)):
                if len(s) - startIndex > 3*(4-len(path)): continue #剪枝
                p = s[startIndex:i+1]
                if(isValid(p)):
                    path.append(p)
                else:continue
                backtrack(s,i+1)
                path.pop()
        backtrack(s,0)
        return result

        

if __name__ ==  "__main__":
    s = Solution()
    a = "025511135"
    print(s.restoreIpAddresses(a))
