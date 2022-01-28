#
# @lc app=leetcode.cn id=1996 lang=python3
#
# [1996] 游戏中弱角色的数量
#

# @lc code=start


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # properties.sort(key=lambda x: (-x[0],x[1]))
        # res = 0
        # maxd = 0 
        # for _,de in properties:
        #     if(maxd > de):
        #         res += 1 
        #     else:
        #         maxd = de 
        # return res   
        properties.sort(key = lambda x: (x[0], -x[1]))
        ans = 0
        st = []
        for _, def_ in properties:
            while st and st[-1] < def_:
                st.pop()
                ans += 1
            st.append(def_)
        return ans

# @lc code=end

