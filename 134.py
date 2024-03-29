class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
        你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
        如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
        说明: 
        如果题目有解，该答案即为唯一答案。
        输入数组均为非空数组，且长度相同。
        输入数组中的元素均为非负数。
        输入: 
        gas  = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        输出: 3
        """
        totalSum = curSum = 0
        startIndex = 0 
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if(curSum < 0):
                startIndex = i+1
                curSum = 0
        if(totalSum < 0 ): return -1
        return startIndex

if __name__ ==  "__main__":
    s = Solution()
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(s.canCompleteCircuit(gas,cost))