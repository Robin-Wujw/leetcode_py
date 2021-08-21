class Solution:
    def permute(self, nums):
        '''
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        '''
        l = []
        result = []
        used = [False] * len(nums)
        def backtrack(nums,used):
            if len(l) == len(nums):
                return result.append(l[:])
            for i in range(len(nums)):
                if used[i] == True:
                    continue    #用过不用了
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
    nums = [0,1]
    print(s.permute(nums))