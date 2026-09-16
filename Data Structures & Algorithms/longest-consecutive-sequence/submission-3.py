class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Consecutives = [[] for i in range(len(nums))]
        nums_2 = set(nums)
        for i in range(len(nums)):
            Val = nums[i]
            if Val - 1 not in nums_2: 
                Consecutives[i].append(Val)
                while 1 == 1:
                    if Val + 1 in nums_2:
                        Val += 1
                        Consecutives[i].append(Val)
                    else:
                        break

        Longest_Length = 0
        for j in range(len(Consecutives)):
            if Longest_Length < len(Consecutives[j]):
                Longest_Length = len(Consecutives[j])
        return Longest_Length
            


