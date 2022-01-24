#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def generate(A):
        #     if len(A) == 2*n:
        #         if valid(A):
        #             ans.append("".join(A))
        #     else:
        #         A.append('(')
        #         generate(A)
        #         A.pop()
        #         A.append(')')
        #         generate(A)
        #         A.pop()

        # def valid(A):
        #     bal = 0
        #     for c in A:
        #         if c == '(': bal += 1
        #         else: bal -= 1
        #         if bal < 0: return False
        #     return bal == 0

        # ans = []
        # generate([])
        # return ans
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
# @lc code=end

