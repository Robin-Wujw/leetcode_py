class Solution:
    """
    给定两个数组，编写一个函数来计算它们的交集。
    """
    def intersection(self, nums1, nums2):
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
            else:
                continue
        result = list(set(result))
        return result
        #return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组