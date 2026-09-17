class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers) - 1
        while L != R: 
            Summation = numbers[L] + numbers[R]
            if Summation < target:
                L += 1
            elif Summation > target:
                R -= 1
            elif Summation == target:
                return [L+1,R+1]