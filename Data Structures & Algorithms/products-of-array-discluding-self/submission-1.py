class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Return = [1] * len(nums)
        prefix = 1 
        postfix = 1

        for i in range(len(nums)):
            Return[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            Return[i] = postfix * Return[i]
            postfix *= nums[i]
        return Return




       

