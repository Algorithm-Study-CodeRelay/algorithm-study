class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums1 리스트의 빈 부분에 nums2 값을 넣는다.
        for i in range(n):
            nums1[m+i] = nums2[i]

        # sort() 함수를 통해 오름차순 정렬한다.
        nums1 = nums1.sort()