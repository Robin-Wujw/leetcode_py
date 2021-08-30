class Solution:
    def subsetsWithDup(self, nums):
        """        
        给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
        输入：nums = [1,2,2]
        输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
        """
        l = []
        res = []
        def backtrack(nums,startIndex):
            res.append(l[:])
            for i in range(startIndex,len(nums)):
                if(i>startIndex and nums[i]==nums[i-1]): continue #我们要对同一树层使用过的元素进行跳过
                l.append(nums[i])
                backtrack(nums,i+1)
                l.pop()
        sorted(nums)
        backtrack(nums,0)
        return res

if __name__ ==  "__main__":
    s = Solution()
    nums = [4,4,4,1,4]
    print(s.subsetsWithDup(nums))