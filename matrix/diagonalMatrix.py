from typing import List


class Solution:
    def diagonalMatrix(self, matrix: List[List[int]]) -> None:
        matrixLen = len(matrix)

        for i in range(matrixLen):
            for j in range(i, matrixLen):
                print(i,j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            print(i)


sol = Solution()
sol.diagonalMatrix([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
# sol.diagonalMatrix([[1,2,3,10],[4,5,6,11],[7,8,9,12]])