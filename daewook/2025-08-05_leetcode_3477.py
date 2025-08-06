# leetcode 3477번 - Fruits Into Baskets II

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        # fruits는 baskets보다 반드시 작거나 같은 값이어야 넣을 수 있음.
        # 따라서, 크기 비교를 통해 들어가는 케이스를 삭제하여 반복문 수행.
        n = len(fruits)
        
        for i in range(n):
            # baskets 삭제를 진행하기 때문에 크기 반영
            for j in range(len(baskets)): 
                if fruits[i] <= baskets[j]:
                    baskets.pop(j)
                    break

        return len(baskets)