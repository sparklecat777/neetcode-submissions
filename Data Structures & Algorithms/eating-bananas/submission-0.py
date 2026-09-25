class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        response = r

        while l <= r:
            midPoint = (l + r) // 2
            timeTaken = 0 
            for i in piles:
                timeTaken += -(-i // midPoint)
            if timeTaken <= h:
                response = midPoint
                r = midPoint - 1
            else: 
                l = midPoint + 1
        return response
                    
                