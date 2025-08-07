class Solution:
    def makeOrderList(self, nl: ListNode) -> List[int]:
        result = []

        while nl != None:
            result.append(nl.val)
            nl = nl.next

        result = result[::-1]
        return result
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        nl1 = self.makeOrderList(l1)
        nl2 = self.makeOrderList(l2)

        n1 = ''.join(str(x) for x in nl1)
        n2 = ''.join(str(x) for x in nl2)

        sum = int(n1) + int(n2)
        result = list(map(int, list(str(sum))))[::-1]

        print(result)

        answer = ListNode()
        cur = answer

        for i in range(len(result)):
            cur.next = ListNode(result[i])
            cur = cur.next

        return answer.next