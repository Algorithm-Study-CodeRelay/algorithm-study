class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)             # 두 리스트를 합치고
        nums1.sort()                    # 파이썬 sort 사용

        for i in range(n):
            del nums1[nums1.index(0)]   # n개의 0을 지움