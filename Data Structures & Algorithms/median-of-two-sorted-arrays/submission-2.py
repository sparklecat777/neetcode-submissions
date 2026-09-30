class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from statistics import median
        
        nums1.extend(nums2)
        return median(nums1)