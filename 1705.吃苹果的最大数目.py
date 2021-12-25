#
# @lc app=leetcode.cn id=1705 lang=python3
#
# [1705] 吃苹果的最大数目
#

# @lc code=start
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        ans = 0
        q = []
        # 最大值，帮助确定天数范围
        max_ = max([max(apples),max(days)])
        for i in range(len(apples)+max_):
            if i < len(apples):
                # 入队
                heapq.heappush(q,(i+days[i],apples[i]))
            while q:
                # 不断出队，直到出现腐烂天数在当前天数之后，且苹果数大于0的
                node_day,node_apple = heapq.heappop(q)
                if node_day > i and node_apple > 0:
                    ans += 1
                    node_apple -= 1
                    if node_apple > 0:
                        heapq.heappush(q,(node_day,node_apple))
                    break
        return ans

# @lc code=end

