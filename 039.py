class Solution:
    def combinationSum(self, candidates, target):
        '''
        给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

        candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
        '''        
        l = []
        result = []
        def backtrack(candidates,target,sum,startIndex):
            if sum > target:
                return 
            if sum == target:
                return result.append(l[:])
            for i in range(startIndex,len(candidates)):
                if sum + candidates[i] > target: return 
                sum = sum + candidates[i]
                l.append(candidates[i])            
                backtrack(candidates,target,sum,i)
                sum -= candidates[i]
                l.pop()
        candidates = sorted(candidates)
        backtrack(candidates,target,0,0)
        return result

if __name__ ==  "__main__":
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates,target))