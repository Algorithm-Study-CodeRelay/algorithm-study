# LeetCode 2348번 Number of Zero-Filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        stack = 0
        answer = []

        # answer 리스트에 연속된 0 스택을 담는다. 
        # 예. 0이 4개 연속으로 담겨있을 경우, 4를 리스트에 추가.
        for i in range(len(nums)):
            if nums[i] == 0:
                stack += 1

            elif stack != 0:
                answer.append(stack)
                stack = 0

            if i+1 == len(nums) and stack != 0:
                answer.append(stack)

        # 해당 subarrays에서 해당 숫자까지의 합을 더하면, 모든 경우의 0 subarrays 개수가 나온다.
        # 예. 4일 경우, 4+3+2+1 = 10 이 된다.
        new_answer = [int(x * (x+1) / 2) for x in answer]

        return sum(new_answer)

