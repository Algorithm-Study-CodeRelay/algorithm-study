class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]: # 바구니에 들어가면
                    del baskets[j]          # 해당 바구니 삭제
                    break
        
        return len(baskets)                 # 남은 바구니의 수 == 남은 과일의 수