# class Solution(object):
#     def findMedianSortedArrays(self,nums1,nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         m = len(nums1)
#         n = len(nums2)
#         if m > n:
#             nums1 ,nums2, m ,n =nums2 , nums1 , n , m
#         if m == 0 :
#             if n %2 ==0:
#                 return (nums2[int((n/2)-1)]+nums2[int(n/2)])/2.0
#             else:
#                 return nums2[int(n/2)]
#         iMin = 0
#         iMax = m
#         half =int((m+n+1) / 2)
#         while iMin <= iMax:
#             i = int((iMin+iMax)/2)
#             j = half -i
#             if i <  m and nums2[j-1] > nums1[i] :
#                 iMin = i + 1
#             elif i > 0 and nums1[i-1]>nums2[j] :
#                 iMax = i - 1
#             else:
#                 if i == 0:
#                     maxLeft = nums2[j-1]
#                 elif j == 0:
#                     maxLeft = nums1[i-1]
#                 else:
#                     maxLeft = max(nums1[i-1],nums2[j-1])

#                 if i == m :
#                     minRight = nums2[j]
#                 elif j == n:
#                     minRight = nums1[i]
#                 else:
#                     minRight = min(nums1[i],nums2[j])

#                 if (m+n) % 2 == 0:
#                     return (maxLeft + minRight) / 2.0
#                 else :
#                     return maxLeft
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。       
        """
        pass

