import numpy as np

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        # 행과 열의 수를 먼저 구한다.
        m = len(matrix)
        n = len(matrix[0])

        # 행과 열 중 더 작은 수를 구한다.
        minimum = min(m, n)

        result = 0

        # dp를 통해 문제 해결함.
        dp = matrix
        
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 0:
                    continue
                
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        numpy_dp = np.array(dp)
        result = np.sum(numpy_dp)

        # 아래 코드도 되긴 하지만, O(n^3)이라 runtime error가 발생함.
        # matrix_np = np.array(matrix)

        # for i in range(1, minimum+1):
        #     # i x i의 개수를 구함.
        #     for j in range(0, m+1-i):
        #         for k in range(0, n+1-i):
        #             if np.sum(matrix_np[j:j+i, k:k+i]) == i ** 2:
        #                 result += 1
        
        return int(result)
