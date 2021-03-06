"""

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000


"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Hash = []
        i = 0
        j = 0
        maxLen = 0
        while j < len(nums):
            if nums[j] == 1:
                Hash.append(1)
                j = j + 1
            else:
                maxLen = max(len(Hash), maxLen)
                Hash = []
                j = j + 1
                i = j

        maxLen = max(len(Hash), maxLen)
        return maxLen