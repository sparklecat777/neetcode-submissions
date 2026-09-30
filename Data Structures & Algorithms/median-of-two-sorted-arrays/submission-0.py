class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        return statistics.median(nums1)