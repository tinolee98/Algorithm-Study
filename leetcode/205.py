# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_char = []
        s_int = []
        t_char = []

        for c in s:
            if c not in s_char:
                s_char.append(c)
            s_int.append(s_char.index(c))

        for i in range(len(t)):
            if t[i] not in t_char:
                t_char.append(t[i])
            if t_char.index(t[i]) != s_int[i]:
                return False
        
        return True