#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
class NumArray:
#     def __init__(self, nums: List[int]):
#         n = len(nums)
#         size = int(n ** 0.5)
#         sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
#         for i, num in enumerate(nums):
#             sums[i // size] += num
#         self.nums = nums
#         self.sums = sums
#         self.size = size

#     def update(self, index: int, val: int) -> None:
#         self.sums[index // self.size] += val - self.nums[index]
#         self.nums[index] = val

#     def sumRange(self, left: int, right: int) -> int:
#         m = self.size
#         b1, b2 = left // m, right // m
#         if b1 == b2:  # 区间 [left, right] 在同一块中
#             return sum(self.nums[left:right + 1])
#         return sum(self.nums[left:(b1 + 1) * m]) + sum(self.sums[b1 + 1:b2]) + sum(self.nums[b2 * m:right + 1])
#线段树
    # def __init__(self, nums: List[int]):
    #     n = len(nums)
    #     self.n = n
    #     self.seg = [0] * (n * 4)
    #     self.build(nums, 0, 0, n - 1)

    # def build(self, nums: List[int], node: int, s: int, e: int):
    #     if s == e:
    #         self.seg[node] = nums[s]
    #         return
    #     m = s + (e - s) // 2
    #     self.build(nums, node * 2 + 1, s, m)
    #     self.build(nums, node * 2 + 2, m + 1, e)
    #     self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    # def change(self, index: int, val: int, node: int, s: int, e: int):
    #     if s == e:
    #         self.seg[node] = val
    #         return
    #     m = s + (e - s) // 2
    #     if index <= m:
    #         self.change(index, val, node * 2 + 1, s, m)
    #     else:
    #         self.change(index, val, node * 2 + 2, m + 1, e)
    #     self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    # def range(self, left: int, right: int, node: int, s: int, e: int) -> int:
    #     if left == s and right == e:
    #         return self.seg[node]
    #     m = s + (e - s) // 2
    #     if right <= m:
    #         return self.range(left, right, node * 2 + 1, s, m)
    #     if left > m:
    #         return self.range(left, right, node * 2 + 2, m + 1, e)
    #     return self.range(left, m, node * 2 + 1, s, m) + self.range(m + 1, right, node * 2 + 2, m + 1, e)

    # def update(self, index: int, val: int) -> None:
    #     self.change(index, val, 0, 0, self.n - 1)

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.range(left, right, 0, 0, self.n - 1)
#树状数组
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index: int, val: int):
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index

    def prefixSum(self, index) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

