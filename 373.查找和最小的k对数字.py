#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#优先队列
        # m, n = len(nums1), len(nums2)
        # ans = []
        # pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        # while pq and len(ans) < k:
        #     _, i, j = heappop(pq)
        #     ans.append([nums1[i], nums2[j]])
        #     if j + 1 < n:
        #         heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        # return ans
#二分查找
        m, n = len(nums1), len(nums2)

        # 二分查找第 k 小的数对和
        left, right = nums1[0] + nums2[0], nums1[m - 1] + nums2[n - 1] + 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            i, j = 0, n - 1
            while i < m and j >= 0:
                if nums1[i] + nums2[j] > mid:
                    j -= 1
                else:
                    cnt += j + 1
                    i += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        pairSum = left

        ans = []
        # 找数对和小于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= pairSum:
                i -= 1
            for j in range(i + 1):
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans

        # 找数对和等于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > pairSum:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == pairSum:
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans
                j -= 1
        return ans
# @lc code=end

