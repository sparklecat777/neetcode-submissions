class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            midPoint = (l + r) // 2
            value = nums[midPoint]

            if value == target:
                return midPoint
            elif value < target:
                l = midPoint + 1
            else: 
                r = midPoint - 1
        
        return -1