class Solution:
    def fourSum(self,nums,target):
        """

        :type nums:  List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret,dict = set(),{}
        numsLen  = len(nums)
        nums.sort()
        for i in range(numsLen):
            for j in range(i+1,numsLen):
                key = nums[i] + nums[j]
                if key not in dict.keys():
                    dict[key]=[(i,j)]
                else:
                    dict[key].append((i,j))

        for i in range(numsLen):
            for j in range(i+1,numsLen):
                temp = target - nums[i] - nums[j]
                if temp in dict.keys():
                    for tempIndex in dict[temp]:
                        if tempIndex[0] > j:
                            ret.add((nums[i],nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]])))
        return [list(i) for i in ret]


