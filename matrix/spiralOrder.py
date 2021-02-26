"""

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        left = 0;
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        # print(left,right,top,bottom)
        res = []

        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4
        return res
