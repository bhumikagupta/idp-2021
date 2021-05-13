class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        max_side_len = 0
        dp = [[ 0 for j in range(col+1)] for i in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
                    max_side_len = max(max_side_len, dp[i][j])
        return max_side_len * max_side_len
