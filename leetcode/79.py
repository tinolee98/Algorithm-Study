# 79. Word Search
# https://leetcode.com/problems/word-search

from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recursion(k, x, y, checked):
            result = 0
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            if k == len(word) - 1:
                return 1
            for dx, dy in d:
                cx, cy = x + dx, y + dy
                if 0 <= cx < len(board) and 0 <= cy < len(board[0]) and board[cx][cy] == word[k+1] and checked[cx][cy] == 0:
                    checked[cx][cy] = 1
                    result = max(result, recursion(k+1, cx, cy, checked))
                    checked[cx][cy] = 0
            return result
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    checked = [[0]*len(board[0]) for _ in range(len(board))]
                    checked[i][j] = 1
                    if recursion(0, i, j, checked) == 1:
                        return True
        
        return False
