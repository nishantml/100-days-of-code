
"""
3. Longest Substring Without Repeating Characters


Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        max_count = []
        Hash = []
        for i in range(len(s)):
            print(i)
            for j in range(i, len(s)):
                if s[j] not in Hash:
                    Hash.append(s[j])
                else:
                    max_count.append(len(Hash))
                    print(Hash)
                    Hash = []
                    break
        return max(max_count)
