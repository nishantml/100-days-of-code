"""

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        direction = 0

        count = 1
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    print(top, i)
                    matrix[top][i] = count
                    count += 1
                top += 1
            elif direction == 1:
                for i in range(top, bottom + 1):
                    matrix[i][right] = count
                    print(i, right)
                    count += 1
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    print(bottom, i)
                    matrix[bottom][i] = count
                    count += 1
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    print(i, left)
                    matrix[i][left] = count
                    count += 1
                left += 1

            direction = (direction + 1) % 4

        return matrix

