class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        freq = [[] for i in range(len(nums)+1)]

        for num, frequency in count.items():
            freq[frequency].append(num)
        
        Return=[]

        for i in range((len(freq)-1),0,-1):
            for j in freq[i]:
                Return.append(j)
                if len(Return) == k:
                    return Return







