#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])
        ans = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                total,num = 0,0
                for l in range(max(i-1,0),min(i+2,m)):
                    for c in range(max(j-1,0),min(j+2,n)):
                        total += img[l][c]
                        num   += 1
                ans[i][j] = total//num        
        return ans 


# @lc code=end

