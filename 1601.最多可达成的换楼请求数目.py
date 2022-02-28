#
# @lc app=leetcode.cn id=1601 lang=python3
#
# [1601] 最多可达成的换楼请求数目
#

# @lc code=start
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        delta = [0] * n#每栋楼的员工变化量
        ans, cnt, zero = 0, 0, n
        #cnt 被选择的请求数量
        #zero delta中0的个数
        def dfs(pos: int) -> None:
            nonlocal ans, cnt, zero
            if pos == len(requests):
                if zero == n:
                    ans = max(ans, cnt)
                return

            # 不选 requests[pos]
            dfs(pos + 1)

            # 选 requests[pos]
            z = zero
            cnt += 1
            x, y = requests[pos]
            zero -= delta[x] == 0 #如果 delta[x] 增加或减少前为0，则将zero 减1
            delta[x] -= 1
            zero += delta[x] == 0
            zero -= delta[y] == 0
            delta[y] += 1
            zero += delta[y] == 0
            dfs(pos + 1)
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1
            zero = z

        dfs(0)
        return ans

# @lc code=end

