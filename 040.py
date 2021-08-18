class Solution:
    def combinationSum2(self, candidates, target):
        """
        给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

        candidates 中的每个数字在每个组合中只能使用一次。
        """
        l = []
        result = []
        def backtrack(candidates,target,sum,startIndex):
            if sum > target: return 
            if sum == target: return result.append(l[:])
            for i in range(startIndex,len(candidates)):
                #单层使用元素去重 i>startIndex 代表不是第一次选
                if(i>startIndex and candidates[i]==candidates[i-1]): continue
                l.append(candidates[i])
                sum += candidates[i]
                backtrack(candidates,target,sum,i+1)
                sum -= candidates[i]
                l.pop()
        candidates = sorted(candidates)
        print(candidates)
        backtrack(candidates,target,0,0)
        return  result
            
if __name__ ==  "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5] 
    target = 8
    print(s.combinationSum2(candidates,target))

