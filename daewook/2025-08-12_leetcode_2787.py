class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        MOD = 10**9 + 7
        
        power_list = []
        i = 1

        # n보다 작은 x제곱 수들을 저장함.
        while (i ** x) <= n:
            power_list.append(i ** x)
            i += 1
    
        # dp 테이블을 만들어서 구함.
        dp = [0] * (n + 1)
        dp[0] = 1

        # power_list 안에 있는 숫자만 역순으로 가서 값을 더하게 됨.
        for power_num in power_list:
            for j in range(n, power_num - 1, -1):
                dp[j] = (dp[j] + dp[j - power_num]) % MOD

        return dp[n]