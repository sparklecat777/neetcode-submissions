class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height, length = len(matrix), len(matrix[0])
        instances = (height * length) - 1 

        l,r = 0, instances
        while l <= r:
            mid = (l + r) // 2
            midVal = matrix[mid // length][mid % length]
            if midVal == target:
                return True
            if midVal < target: 
                l = mid + 1
            if midVal > target:
                r = mid - 1 

        return False
            