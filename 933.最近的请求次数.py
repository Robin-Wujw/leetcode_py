#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.tlist = deque()

    def ping(self, t: int) -> int:
        self.tlist.append(t)
        while(self.tlist[0]<t-3000):
            self.tlist.popleft()
        return len(self.tlist)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

