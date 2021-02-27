"""
74. Search a 2D Matrix
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if target in mat:
                return True
