class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1 :
            return 0        
        
        maxi = 0
        for i in range(1, len(matrix)) :
            for j in range(1, len(matrix[0])) :
                if int(matrix[i][j]) != 0 :
                    matrix[i][j] = min(int(matrix[i][j-1]), int(matrix[i-1][j]), int(matrix[i-1][j-1])) + 1
                    maxi = max(maxi, matrix[i][j])
                    print maxi
        
        if maxi==0:
            for i in range(0, len(matrix[0])) :
                if matrix[0][i] == "1" :
                    return 1
            for i in range(0, len(matrix)) :
                if matrix[i][0] == "1" :
                        return 1   
        
        return maxi*maxi
