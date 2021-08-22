class Solution:
    def permuteUnique(self, nums):
        """
         给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
        """
        l = []
        result = []
        used = [False] * len(nums)
        def backtrack(nums,used):
            if len(l) == len(nums):
                return result.append(l[:])
            for i in range(len(nums)):
                if used[i] == True:
                    continue    #用过不用了
                if(i>0 and used[i-1] == False and nums[i]==nums[i-1]): continue #used[i-1] == False 表示同层
                l.append(nums[i])
                used[i] = True
                backtrack(nums,used)
                l.pop()
                used[i] = False
        nums = sorted(nums)
        backtrack(nums,used)
        return result


if __name__ ==  "__main__":
    s = Solution()
    nums = [1,1,2]
    print(s.permuteUnique(nums))