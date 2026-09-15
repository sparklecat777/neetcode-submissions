class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Seen = set() 
        for i in nums:
            if i in Seen:
                return True
            Seen.add(i)
        return False