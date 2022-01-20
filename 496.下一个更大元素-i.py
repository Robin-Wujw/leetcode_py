#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # m, n = len(nums1), len(nums2)
        # res = [0] * m
        # for i in range(m):
        #     j = nums2.index(nums1[i])
        #     k = j + 1
        #     while k < n and nums2[k] < nums2[j]:
        #         k += 1
        #     res[i] = nums2[k] if k < n else -1
        # return res
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]


# @lc code=end

