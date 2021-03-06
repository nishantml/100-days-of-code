"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            count = 0;

            while count + i <= len(s):
                print(s[count:count + i])
                if s[count:count + i] == s[count:count + i][::-1]:
                    return s[count:count + i]
                count += 1
        return -1

