# LeetCode 3번 Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0
        str_list = list(s)
        print(str_list)

        tmp = 0
        before = []

        if str_list == ' ':
            return 1

        for i in str_list:

            # 앞에서 안나오면 1 증가 !
            if i not in before:
                tmp += 1
                before.append(i)

            # 근데 바로 직전에 같은게 나왔네 ? 리셋
            elif before[-1] == i:
                result = max(result, tmp)
                tmp = 1
                before = []
                before.append(i)
            
            # 그거말고 중간에 같은게 나온적 있어 ! 그앞만 지울래 !
            else:
                result = max(result, tmp)
                start_index = before.index(i)
                before = before[start_index+1:]
                before.append(i)
                tmp = len(before)

        result = max(result, tmp)
        
        return result