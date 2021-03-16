"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.legth <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return nums

        Hash = dict()
        lst = []

        for val in nums:
            if val not in Hash:
                Hash[val] = 1
            else:
                Hash[val] += 1

        # sorting dict keys
        sorted_dict = {}
        sorted_keys = sorted(Hash, key=Hash.get)

        for w in reversed(sorted_keys):
            sorted_dict[w] = Hash[w]

        count = 1
        for w in sorted_dict.keys():
            # print(w)
            lst.append(w)
            if count == k:
                return lst
            count += 1
        # print(Hash)
        # print(sorted_dict)
