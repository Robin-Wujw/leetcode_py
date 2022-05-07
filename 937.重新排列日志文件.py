#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # def trans(log: str) -> tuple:
        #     a, b = log.split(' ', 1)
        #     return (0, b, a) if b[0].isalpha() else (1,)

        # logs.sort(key=trans)  # sort 是稳定排序
        # return logs
        alpha, num = [], []
        for log in logs:
            log_split = log.split()
            if log_split[1][0].isalpha():
                alpha.append([log[len(log_split[0])+1:], log])
            else:
                num.append(log)
        alpha.sort(key = lambda x: [x[0], x[1]])
        return [x[1] for x in alpha] + num
# @lc code=end

