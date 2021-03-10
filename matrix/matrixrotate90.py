from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        newM = []
        for i in range(colLen):
            tem = []
            for j in range(rowLen - 1, 0 - 1, -1):
                # print(matrix[j][i])
                tem.append(matrix[j][i])
            newM.append(tem)

        print('Older matrix')
        for row in matrix:
            print(row)
        print('Matrix after 90 degree rotate')
        for row in newM:
            print(row)


sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
sol.rotate([[1,2,3,10],[4,5,6,11],[7,8,9,12]])