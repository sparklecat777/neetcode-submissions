class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i != j:
                    Value = nums[i]+nums[j]
                    if Value == target:
                        Return_List = [i,j]
                        return Return_List
        
