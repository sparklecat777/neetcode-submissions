class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattenedMatrix = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flattenedMatrix.append(matrix[i][j])
        
        l,r = 0, len(flattenedMatrix) - 1
        while l <= r:
            midPoint = (l + r) // 2
            value = flattenedMatrix[midPoint]

            if value == target:
                return True
            elif value < target:
                l = midPoint + 1
            else: 
                r = midPoint - 1
        
        return False



            