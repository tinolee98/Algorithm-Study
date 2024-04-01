# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/?envType=daily-question&envId=2024-04-01

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: x != "", s.split(" ")))[::-1][0])