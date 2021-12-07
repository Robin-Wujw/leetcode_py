class Solution:
    def replaceSpace(self, s: str) -> str:
        res = list(s)
        for i in range(len(res)):
            if(res[i] == " "):
                res[i] = "%20"
        print("".join(res))
        
if __name__ == "__main__":
    s = "we are friend"
    a = Solution()
    a.replaceSpace(s)