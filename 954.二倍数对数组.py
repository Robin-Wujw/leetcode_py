#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#

# @lc code=start
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:  # 无法找到足够的 2x 与 x 配对
                return False
            cnt[2 * x] -= cnt[x]
        return True
# @lc code=end

