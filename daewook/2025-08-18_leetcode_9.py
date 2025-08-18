# LeetCode 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # x를 리스트로 분리
        x_list = list(str(x))
        # x를 reverse하여 저장함
        x_reverse = x_list[::-1]

        # 두 리스트를 비교하여 값이 다르면, palindrome이 아님.
        for i in range(len(x_list)):
            if x_list[i] != x_reverse[i]:
                return False
            
        return True