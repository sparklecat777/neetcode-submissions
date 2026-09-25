class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0 , len(nums) - 1

        while L < R:
            m = (L + R) // 2
            if nums[m] > nums[R]:
                L = m + 1
            else:
                R = m
        
        pivot = L

        def binarySearch(left: int, right: int):
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return -1
        
        result = binarySearch(0, pivot - 1)
        if result != -1:
            return result
        
        return binarySearch(pivot, len(nums) - 1)