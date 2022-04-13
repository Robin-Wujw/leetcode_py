#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
from secrets import choice


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if(val in self.indices):
            return False
        index = len(self.nums)
        self.indices[val] = index
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.indices):
            return False
        index = self.indices[val] #先把要remove那一位的index取出来
        self.nums[index] = self.nums[-1] #把最后一位的值放到index位置 相当于代替了
        self.indices[self.nums[-1]] = index #把最后一位的值的indices 改一下
        self.nums.pop() #删除操作
        del self.indices[val]   #删除操作
        return True
    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

