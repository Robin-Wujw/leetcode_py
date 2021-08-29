class Solution:
    def subsets(self, nums):
        """
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

        解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
        示例 1：
        输入：nums = [1,2,3]
        输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        """
        l = []
        res = []
        def backtrack(nums,startIndex):
            res.append(l[:])
            for i in range(startIndex,len(nums)):
                l.append(nums[i])
                backtrack(nums,i+1)
                l.pop()
        backtrack(nums,0)
        return res


if __name__ ==  "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))