class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        # 곱한 숫자가 너무 커질 경우, 모듈러 연산을 통해 숫자를 줄임.
        MOD = 10**9 + 7

        # n을 이진수로 만들어 표현하고, 그후 2의 거듭제곱을 하여 powers 리스트를 완성하면 된다.
        binary_n = f"{n:b}"
        
        # 0b를 뗀 숫자를 리스트로 만들어 역순으로 정렬 (오름차순이라고 설명함))
        powers = list(binary_n)[::-1]

        # 2의 거듭제곱을 곱하여 실제 숫자로 만듦
        for i in range(len(powers)):
            powers[i] = int(powers[i]) * (2 ** i)

        # 0을 모두 삭제함.
        powers = list(filter(lambda x: x != 0, powers))
        
        # 이중 for문을 통하여, queries에 있는 값의 범위를 곱한 것이 최종 결과가 된다.
        answer = []
        for i in range(len(queries)):
            a, b = queries[i][0], queries[i][1]
            
            result = 1
            for j in range(a, b+1):
                result = (result * powers[j]) % MOD
            
            answer.append(result)
        
        return answer

        